# -*- coding: utf-8 -*-

__author__ = 'Sandeep S <codereverser@gmail.com>'
__date__ = '04-July-2014'

from ..client import Rel
from .gedcomxapplicationstate import GedcomxApplicationState


class PlaceDescriptionState(GedcomxApplicationState):
    """
    PlaceDescriptionState:
    """

    def __init__(self, session, request, response, accessToken, stateFactory):
        super(PlaceDescriptionState, self).__init__(session, request, response, accessToken, stateFactory)

    def reconstruct(self, request, response):
        return PlaceDescriptionState(self.session, request, response, self.accessToken, self.stateFactory)

    def getMainDataElement(self):
        return self.getPlaceDescription()

    def getSelfRel(self):
        return Rel.DESCRIPTION

    def getPlaceDescription(self):
        if self.entity is not None and len(self.entity.places) > 0:
            return self.entity,places[0]

    def readChildren(self):
        link = self.getLink(Rel.CHILDREN)
        if link is None or link.href == "":
            return None

        request = self.createAuthenticatedGedcomxRequest("GET", url=link.href)
        return self.stateFactory.buildPlaceDescriptionState(self.session, request, self.invoke(request), self.accessToken)