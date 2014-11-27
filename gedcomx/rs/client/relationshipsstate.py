# -*- coding: utf-8 -*-

from ...gedcomx import Gedcomx
from ...relationship import Relationship
from ...types import RelationshipType
from ..client import Rel
from .gedcomxapplicationstate import GedcomxApplicationState



class RelationshipsState(GedcomxApplicationState):

    def __init__(self, session, request, response, access_token, state_factory):
        super(RelationshipsState, self).__init__(session, request, response, access_token, state_factory)

    def reconstruct(self, request, response):
        return RelationshipsState(self.session, request, response, self.accessToken, self.stateFactory)


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

    def addRelationship(self, relationship):
        entity = Gedcomx()
        entity.relationships.append(relationship)
        request = self.createAuthenticatedGedcomxRequest("POST", url=self.getSelfUri())
        self.stateFactory.buildRelationshipState(self.session, request, self.invoke(request), self.accessToken)

    def addSpouseRelationShip(self, person1, person2):
        relationship = Relationship()
        relationship.person1 = person1.getLink(Rel.PERSON)
        relationship.person2 = person2.getLink(Rel.PERSON)
        relationship.type = RelationshipType.Couple
        self.addRelationship(relationship)

    def addSpouseRelationShip(self, parent, child):
        relationship = Relationship()
        relationship.person1 = parent.getLink(Rel.PERSON)
        relationship.person2 = child.getLink(Rel.PERSON)
        relationship.type = RelationshipType.ParentChild
        self.addRelationship(relationship)

