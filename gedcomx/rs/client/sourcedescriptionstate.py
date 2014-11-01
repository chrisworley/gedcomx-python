# -*- coding: utf-8 -*-

__author__ = 'Sandeep S <codereverser@gmail.com>'
__date__ = '04-July-2014'


from ...gedcomx import Gedcomx
from .gedcomxapplicationstate import GedcomxApplicationState
import json

class SourceDescriptionState(GedcomxApplicationState):

    def __init__(self, session, request, response, accessToken, stateFactory):
        super(SourceDescriptionState, self).__init__(session, request, response, accessToken, stateFactory)

    def reconstruct(self, request, response):
        SourceDescriptionState(self.session, request, response, self.accessToken, self.stateFactory)

    def getSelfRel(self):
        return Rel.SOURCEREFERENCE

    def getSourceDescription(self):
        if self.entity is not None and len(self.entity.sourceDescriptions) > 0:
            return self.entity.sourceDescriptions[0]

    def getMainDataElement(self):
        return self.getSourceDescription()

    def update(self, description):
        entity = Gedcomx()
        entity.sourceDescriptions.append(description)
        request = self.createAuthenticatedGedcomxRequest("POST", self.getSelfUri())
        request.data = json.dumps(entity.to_dict())
        return self.stateFactory.buildSourceDescriptionState(self.session, request, self.invoke(request), self.accessToken)

