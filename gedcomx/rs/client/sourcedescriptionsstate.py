# -*- coding: utf-8 -*-

import json
from ...gedcomx import Gedcomx
from ..client import Rel
from .gedcomxapplicationstate import GedcomxApplicationState
from .personstate import PersonState


class SourceDescriptionsState(GedcomxApplicationState):

    def __init__(self, session, request, response, access_token, state_factory):
        super(SourceDescriptionsState, self).__init__(session, request, response, access_token, state_factory)

    def reconstruct(self, request, response):
        return SourceDescriptionsState(self.session, request, response, self.accessToken, self.stateFactory)


    def getMainDataElement(self):
        return self.entity

    def getCollections(self):
        if self.entity is not None:
            return self.entity.collections

    def getSourceDescriptions(self):
        if self.entity is not None:
            return self.entity.sourceDescriptions


    def readCollection(self):
        link = self.getLink(Rel.COLLECTION)

        if link is None or link.href == "":
            return None

        request = self.createAuthenticatedGedcomxRequest("GET", url=link.href)
        return self.stateFactory.buildCollectionState(self.session, request, self.invoke(request), self.accessToken)

    def addSourceDescription(self, sourceDescription):
        link = self.getLink(Rel.SELF)

        if link is None or link.href == "":
            return None
        entity = Gedcomx()
        entity.sourceDescriptions.append(sourceDescription)

        request = self.createAuthenticatedGedcomxRequest("POST", url=link.href)
        request.data = json.dumps(entity.to_dict())
        return self.stateFactory.buildPersonState(self.session, request, self.invoke(request), self.accessToken)


