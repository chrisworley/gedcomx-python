# -*- coding: utf-8 -*-

__author__ = 'Sandeep S <codereverser@gmail.com>'
__version__ = '0.1'
__date__ = '03-July-2014'

import requests

from ..client import MEDIA_TYPES
from .personstate import PersonState
from .collectionstate import CollectionState
from .collectionsstate import CollectionsState
from .ancestryresultsstate import AncestryResultsState
from .descendancyresultsstate import DescendancyResultsState
from .agentstate import AgentState
from .personsstate import PersonsState
from .personchildrenstate import PersonChildrenState
from .personparentsstate import PersonParentsState
from .personspousesstate import PersonSpousesState
from .recordstate import RecordState
from .recordsstate import RecordsState
from .sourcedescriptionsstate import SourceDescriptionsState
from .sourcedescriptionstate import SourceDescriptionState
from .placedescriptionsstate import PlaceDescriptionsState
from .placedescriptionstate import PlaceDescriptionState
from .personsearchresultsstate import PersonSearchResultsState
from .relationshipstate import RelationshipState
from relationshipsstate import RelationshipsState


class StateFactory(object):

    def __init__(self, session=None, accessToken=None):
        """
        :param requests.Session session: Session
        :param str accessToken: oAuth accessToken
        """
        self.session = session
        self.accessToken = accessToken

        if self.session is None:
            self.session = requests.session()

    def prepareRequestAndResponse(self, url, method="GET", session=None):
        if session is None:
            session = self.session
        header = {'Accept': MEDIA_TYPES.GEDCOMX_MEDIA_TYPE }
        request = requests.Request(method, url, headers=header)
        prep = session.prepare_request(request)
        response = session.send(prep)
        return request, response

    def newPersonState(self, url):
        request, response = self.prepareRequestAndResponse(url)
        return self.buildPersonState(self.session, request, response, None)

    def buildPersonState(self, session, request, response, accessToken):
        return PersonState(session, request, response, accessToken, self)



    def buildAncestryResultsState(self, session, request, response, accessToken):
        return AncestryResultsState(session, request, response, accessToken, self)

    def newAncestryResultsState(self, url):
        request, response = self.prepareRequestAndResponse(url)
        return self.buildAncestryResultsState(self.session, request, response, None)

    def buildDescendancyResultsState(self, session, request, response, accessToken):
        return DescendancyResultsState(session, request, response, accessToken, self)

    def newDescendancyResultsState(self, url):
        request, response = self.prepareRequestAndResponse(url)
        return self.buildDescendancyResultsState(self.session, request, response, None)

    def buildCollectionState(self, session, request, response, accessToken):
        return CollectionState(session, request, response, accessToken, self)

    def newCollectionState(self, url):
        request, response = self.prepareRequestAndResponse(url)
        return self.buildCollectionState(self.session, request, response, None)

    def buildCollectionsState(self, session, request, response, accessToken):
        return CollectionsState(session, request, response, accessToken, self)

    def newCollectionsState(self, url):
        request, response = self.prepareRequestAndResponse(url)
        return self.buildCollectionState(self.session, request, response, None)

    def buildPersonChildrenState(self, session, request, response, accessToken):
        return PersonChildrenState(session, request, response, accessToken, self)

    def buildPersonParentsState(self, session, request, response, accessToken):
        return PersonParentsState(session, request, response, accessToken, self)

    def buildPersonSearchResultsState(self, session, request, response, accessToken):
        return PersonSearchResultsState(session, request, response, accessToken, self)

    def buildPersonsState(self, session, request, response, accessToken):
        return PersonsState(session, request, response, accessToken, self)

    def newPersonsState(self, url):
        request, response = self.prepareRequestAndResponse(url)
        return self.buildPersonsState(self.session, request, response, self.accessToken)

    def buildPlaceDescriptionState(self, session, request, response, accessToken):
        return PlaceDescriptionState(session, request, response, accessToken, self)

    def buildPlaceDescriptionsState(self, session, request, response, accessToken):
        return PlaceDescriptionsState(session, request, response, accessToken, self)

    def buildRelationshipState(self, session, request, response, accessToken):
        return RelationshipState(session, request, response, accessToken, self)

    def buildRelationshipsState(self, session, request, response, accessToken):
        return RelationshipsState(session, request, response, accessToken, self)


