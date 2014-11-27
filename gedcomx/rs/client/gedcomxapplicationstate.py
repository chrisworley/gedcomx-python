# -*- coding: utf-8 -*-

import abc
import json
import requests

from ...link import Link
from ..client import GedcomxApplicationException, MEDIA_TYPES, Rel
from .util import loadEmbeddedLinks
from ...gedcomx import Gedcomx


class GedcomxApplicationState:
    """

    """

    __metaclass__ = abc.ABCMeta

    def __init__(self, session, request, response, accessToken, stateFactory):
        """
        Constructor

        :param requests.Request request: The request object from the session.
        :param requests.Response response: The response object from the last request.
        :param str accessToken: The OAuth2 access token
        :param StateFactory stateFactory: statefactory class
        :ivar requests.Response entity: Entity
        :return:
        """

        self.session = session
        self.request = request
        self.response = response
        self.accessToken = accessToken
        self.stateFactory = stateFactory

        self.links = {}

        self.entity = self.loadEntityConditionally(self.response)

        self.links = self.loadLinks(self.response, self.entity)

    def loadEntityConditionally(self, response):
        """Load the entity corresponding to the application state from the server response.

        :param requests.Response response: Response from the server
        :return: None
        """
        if self.request.method not in ('HEAD', 'OPTIONS') and response.status_code == 200:
            return self.loadEntity(response)
        else:
            return None

    def loadEntity(self, response):
        """Load the entity corresponding to the application state from the server response.

        :param requests.Response response: Response from the server
        :return Gedcomx: Gedcomx object
        """
        return Gedcomx(response.json())

    @abc.abstractmethod
    def getMainDataElement(self):
        pass

    @abc.abstractmethod
    def reconstruct(self, request, response):
        pass

    def loadLinks(self, response, entity):

        links = {}

        location = response.headers.get('Location', None)
        if location is not None:
            links[Rel.SELF] = Link()
            links[Rel.SELF].rel = 'self'
            links[Rel.SELF].href = location

        headers = response.headers.keys()
        for header in headers:
            header_data = response.headers.get(header, None)
            if header_data is not None and isinstance(header_data, dict) and 'rel' in header_data:
                rel = header_data['rel']
                link = Link(rel)
                links[rel] = link

        if entity is not None and hasattr(entity, 'links'):
            for rel, link in entity.links.items():
                links[rel] = link

        main_element = self.getMainDataElement()
        if main_element not in (entity, None) and hasattr(main_element, 'links'):
            for rel, link in main_element.links.items():
                links[rel] = link

        return links

    def getSelfRel(self):
        return Rel.SELF

    def getUri(self):
        return self.request.url

    def getLink(self, rel):
        """Returns the link with the specified relation identifier.

        :param rel: The link relation identifier to search for.
        :return: returns Link object if found, otherwise None
        """
        return self.links.get(rel)

    def getSelfUri(self):

        self_rel = self.getSelfRel()
        link = None
        if self_rel is not None:
            link = self.getLink(self_rel)

        if link is None:
            link = self.getLink(Rel.SELF)

        if link is not None and link.href:
            return link.href
        else:
            return self.getUri()

    def hasClientError(self):
        return 400 <= self.response.status_code < 500

    def hasServerError(self):
        return 500 <= self.response.status_code < 600

    def hasError(self):
        return self.hasClientError() or self.hasServerError()

    def getHeaders(self):
        return self.response.headers

    def get(self, request_type="GET"):
        request = self.createAuthenticatedRequest(request_type)
        if 'Accept' in self.request.headers:
            request.headers['Accept'] = self.request.headers['Accept']
        return self.reconstruct(request, self.invoke(request))

    def head(self):
        return self.get(request_type="HEAD")

    def delete(self):
        return self.get(request_type="DELETE")

    def options(self):
        return self.get(request_type="OPTIONS")

    def put(self, entity):
        request = self.createAuthenticatedRequest("PUT")
        if 'Accept' in self.request.headers:
            request.headers['Accept'] = self.request.headers['Accept']
        if 'Content-Type' in self.request.headers:
            request.headers['Content-Type'] = self.request.headers['Content-Type']
        request.data = json.dumps(entity.to_dict())
        return self.reconstruct(request, self.invoke(request))

    def ifSuccessful(self):
        if self.hasError():
            raise GedcomxApplicationException("Unsuccessful %s to %s" %(self.request.method, self.getUri()))
        return self

    def authenticateViaOAuth2Password(self, username, password, client_id, client_secret=None):
        data = {'grant_type': "password",
                'username': username,
                'password': password,
                'client_id' : client_id}
        if client_secret is not None:
            data['client_secret'] = client_secret

        return self.authenticateViaOAuth2(data)

    def authenticateViaOAuth2AuthCode(self, auth_code, redirect_uri, client_id, client_secret=None):
        data = {'grant_type': 'authorization_code',
                'code': auth_code,
                'redirect_uri': redirect_uri,
                'client_id': client_id}

        if client_secret is not None:
            data['client_secret'] = client_secret

        return self.authenticateViaOAuth2(data)

    def authenticateViaOAuth2ClientCredentials(self, client_id, client_secret):
        data = {'grant_type': 'client_credentials',
                'client_id': client_id,
                'client_secret': client_secret}

        return self.authenticateViaOAuth2(data)

    def authenticateViaOAuth2(self, data):
        token_link = self.getLink(Rel.OAUTH2_TOKEN)
        if token_link is None or token_link.href == "":
            raise GedcomxApplicationException("No OAuth2 token URI supplied for resource at {%s}" % self.getUri())

        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/x-www-form-urlencoded'}
        request = self.createRequest(method="POST", url=token_link.href, headers=headers, data=data)
        response = self.invoke(request)

        if 200 <= response.status_code < 300:
            tokens = json.loads(response.content)

            if 'token' in tokens:
                self.accessToken = tokens['token']
            elif 'access_token' in tokens:
                self.accessToken = tokens['access_token']
            else:
                raise GedcomxApplicationException('Illegal access token response: no access_token provided.', data)
            return self
        else:
            raise GedcomxApplicationException('Unable to obtain an access token.', data)

    def createRequest(self, method, url, headers=None, data=None):
        return requests.Request(method, url, headers=headers, data=data)

    def createAuthenticatedRequest(self, method):
        request = self.createRequest(method, self.getUri())
        if self.accessToken is not None:
            request.headers['Authorization'] = "Bearer %s" % self.accessToken
        return request

    def createAuthenticatedGedcomxRequest(self, method, url = None):
        request = self.createAuthenticatedRequest(method);
        request.headers['Accept'] = MEDIA_TYPES.GEDCOMX_MEDIA_TYPE
        request.headers['Content-Type'] = MEDIA_TYPES.GEDCOMX_MEDIA_TYPE
        if url is not None:
            request.url = url
        return request

    def createAuthenticatedAtomRequest(self, method, url = None):
        request = self.createAuthenticatedRequest(method);
        request.headers['Accept'] = MEDIA_TYPES.ATOM_MEDIA_TYPE
        request.headers['Content-Type'] = MEDIA_TYPES.ATOM_MEDIA_TYPE
        if url is not None:
            request.url = url
        return request


    def invoke(self, request):
        """
        Sends a http request to a server and returns the response. Placeholder function
        set to easily modify, if more features like cookie support is required in the future.
        :param request: Request to be sent to the server
        :return: Response from the server
        """
        prep = self.session.prepare_request(request)
        return self.session.send(prep)

    def includeEmbeddedResources(self, entity):
        """

        :param Gedcomx entity:
        :return:
        """
        for link in loadEmbeddedLinks(entity):
            self.embed(link, entity)

    def embed(self, link, entity):
        """

        :param link:
        :param Gedcomx entity: Gedcomx entity
        :return:
        """
        if link.href != "":
            request = self.createAuthenticatedGedcomxRequest("GET", url=link.href)
            response = self.invoke(request)
            if response.status_code == 200:
                entity.embed(Gedcomx(response.json()))

    def loadEmbeddedResources(self, rels=[]):
        self.includeEmbeddedResources(self.entity)
        for rel in rels:
            link = self.getLink(rel)
            if link is not None and link.href != "":
                self.embed(link, self.entity)
        return self

    def loadConclusions(self):
        return self.loadEmbeddedResources(rels=[Rel.CONCLUSIONS])

    def loadSourceReferences(self):
        return self.loadEmbeddedResources(rels=[Rel.SOURCE_REFERENCES])

    def MediaReferences(self):
        return self.loadEmbeddedResources(rels=[Rel.MEDIA_REFERENCES])

    def loadEvidenceReferences(self):
        return self.loadEmbeddedResources(rels=[Rel.EVIDENCE_REFERENCES])

    def loadPersonalReferences(self):
        return self.loadEvidenceReferences()

    def loadNotes(self):
        return self.loadEmbeddedResources(rels=[Rel.NOTES])

    def loadParentRelationships(self):
        return self.loadEmbeddedResources(rels=[Rel.PARENT_RELATIONSHIPS])

    def loadSpouseRelationShips(self):
        return self.loadEmbeddedResources(rels=[Rel.SPOUSE_RELATIONSHIPS])

    def loadChildRelationShips(self):
        return self.loadEmbeddedResources(rels=[Rel.CHILD_RELATIONSHIPS])

    def readPersonForCurrentUser(self):
        personLink = self.getLink(Rel.CURRENT_USER_PERSON)
        if personLink is None or personLink.href == "":
            return None
        request = self.createAuthenticatedGedcomxRequest("GET", url=personLink.href)
        return self.stateFactory.buildPersonState(self.session, request, self.invoke(request), self.accessToken)

    def readPage(self, rel):
        link = self.getLink(rel)
        if link is None or link.href == "":
            return None

        request = self.createAuthenticatedRequest("GET")
        accept = self.request.headers.get('accept')
        content = self.request.headers.get('content-type')

        request.headers = self.request.headers
        request.url = link.href

        self.reconstruct(request, self.invoke(request))

    def readNextPage(self):
        return self.readPage(Rel.NEXT)

    def readPreviousPage(self):
        return self.readPage(Rel.PREVIOUS)

    def readFirstPage(self):
        return self.readPage(Rel.FIRST)

    def readLastPage(self):
        return self.readPage(Rel.LAST)
