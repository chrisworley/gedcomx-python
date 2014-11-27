# -*- coding: utf-8 -*-

from ..client import Rel
from .gedcomxapplicationstate import GedcomxApplicationState
from .util.ancestrytree import AncestryTree

class AncestryResultsState(GedcomxApplicationState):
    """
    AncestryResultsState:
    """

    def __init__(self, session, request, response, accessToken, stateFactory):
        super(AncestryResultsState, self).__init__(session, request, response, accessToken, stateFactory)

    def reconstruct(self, request, response):
        return AncestryResultsState(self.session, request, response, self.accessToken, self.stateFactory)

    def getMainDataElement(self):
        return self.entity

    def getSelfRel(self):
        return Rel.ANCESTRY

    def getTree(self):
        if self.entity:
            return AncestryTree(self.entity)

    def readPerson(self, ancestorNumber):
        tree = self.getTree()
        if tree is None:
            return None
        ancestor = tree.getAncestor(ancestorNumber)
        if ancestor is None:
            return None

        link = ancestor.getPerson().getLink(Rel.PERSON)
        if link is None or link.href == "":
            link = ancestor.getPerson().getLink(Rel.SELF)

        if link is None or link.href == "":
            return None

        request = self.createAuthenticatedGedcomxRequest("GET", link.href)
        return self.stateFactory.buildPersonsState(self.session, request, self.invoke(request), self.accessToken)