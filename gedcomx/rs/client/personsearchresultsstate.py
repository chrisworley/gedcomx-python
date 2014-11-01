# -*- coding: utf-8 -*-

__author__ = 'Sandeep S <codereverser@gmail.com>'
__date__ = '04-July-2014'

from ..client import Rel, GedcomxApplicationException
from .gedcomxapplicationstate import GedcomxApplicationState


class PersonSearchResultsState(GedcomxApplicationState):

    def __init__(self, session, request, response, accessToken, stateFactory):
        super(PersonSearchResultsState, self).__init__(session, request, response, accessToken, stateFactory)

    def reconstruct(self, request, response):
        return PersonSearchResultsState(self.session, request, response, self.accessToken, self.stateFactory)

    def getMainDataElement(self):
        return self.entity

    def getResults(self):
        return self.entity

    def readPerson(self, person):
        link = person.getLink(Rel.PERSON)
        if link is None:
            link = person.getLink(Rel.SELF)

        if link is None or link.href == "":
            return None

        request = self.createAuthenticatedGedcomxRequest("GET", url=link.href)
        self.stateFactory.buildPersonState(self.session, request, self.invoke(request), self.accessToken)


