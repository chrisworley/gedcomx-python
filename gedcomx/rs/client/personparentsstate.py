# -*- coding: utf-8 -*-

from ..client import Rel, GedcomxApplicationException
from .gedcomxapplicationstate import GedcomxApplicationState

class PersonParentsState(GedcomxApplicationState):
    """PersonParentState"""

    def __init__(self, session, request, response, accessToken, stateFactory):
        super(PersonParentsState, self).__init__(session, request, response, accessToken, stateFactory)

    def reconstruct(self, request, response):
        return PersonParentsState(self.session, request, response, self.accessToken, self.stateFactory)

    def getMainDataElement(self):
        return self.entity

    def getPersons(self):
        if self.entity is not None:
            return self.entity.persons
        else:
            return None

    def getRelationShips(self):
        """

        :return:
        :rtype: ListProperty(Relationship)
        """
        if self.entity is not None:
            return self.entity.relationships
        return None

    def findRelationShipTo(self, parent):
        """
        Find the relationship to the child.
        :param Person parent: Object referring to the parent.
        :return:
        """
        relationships = self.getRelationShips()
        """:type : ListProperty(Relationship)"""

        if relationships is None or parent.id == "":
            return None

        for relationship in relationships:
            if relationship.person1.resource.endswith(parent.id):
                return relationship
        return None

    def readPerson(self):
        link = self.getLink(Rel.PERSON)
        if link is None or link.href == "":
            return None

        request = self.createAuthenticatedGedcomxRequest("GET", url=link.href)
        return self.stateFactory.buildPersonState(self.session, request, self.invoke(request), self.accessToken)

    def readParent(self, parent):
        """

        :param Person parent: Parent
        :return:
        """
        link = parent.getLink(Rel.PERSON)
        if link is None:
            link = parent.getLink(Rel.SELF)

        if link is None or link.href == "":
            return None

        request = self.createAuthenticatedGedcomxRequest("GET", url=link.href)
        return self.stateFactory.buildPersonState(self.session, request, self.invoke(request), self.accessToken)

    def readRelationship(self, relationship):

        link = relationship.getLink(Rel.RELATIONSHIP)
        if link is None:
            link = relationship.getLink(Rel.SELF)

        if link is None or link.href == "":
            return None

        request = self.createAuthenticatedGedcomxRequest("GET", url=link.href)
        return self.stateFactory.buildRelationshipState(self.session, request, self.invoke(request), self.accessToken)

    def removeRelationship(self, relationship):
        link = relationship.getLink(Rel.RELATIONSHIP)
        if link is None:
            link = relationship.getLink(Rel.SELF)

        if link is None or link.href == "":
            raise GedcomxApplicationException("Unable to remove relationship: missing link.")

        request = self.createAuthenticatedGedcomxRequest("DELETE", url=link.href)
        return self.stateFactory.buildRelationshipState(self.session, request, self.invoke(request), self.accessToken)

    def removeRelationshipTo(self, child):
        relationship = self.findRelationShipTo(child)
        if relationship is None:
            raise GedcomxApplicationException("Unable to remove relationship: not found.")

        return self.removeRelationship(child)
