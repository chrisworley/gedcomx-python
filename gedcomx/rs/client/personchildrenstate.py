# -*- coding: utf-8 -*-

__author__ = 'Sandeep S <codereverser@gmail.com>'
__date__ = '04-July-2014'

from ..client import Rel, GedcomxApplicationException
from .gedcomxapplicationstate import GedcomxApplicationState

class PersonChildrenState(GedcomxApplicationState):
    """PersonChildrenState"""

    def __init__(self, session, request, response, accessToken, stateFactory):
        super(PersonChildrenState, self).__init__(session, request, response, accessToken, stateFactory)

    def reconstruct(self, request, response):
        return PersonChildrenState(self.session, request, response, self.accessToken, self.stateFactory)

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

    def findRelationShipTo(self, child):
        """
        Find the relationship to the child.
        :param Person child: Object referring to the child.
        :return:
        """
        relationships = self.getRelationShips()
        """:type : ListProperty(Relationship)"""

        if relationships is None or child.id == "":
            return None

        for relationship in relationships:
            if relationship.person2.resource.endswith(child.id):
                return relationship
        return None

    def readPerson(self):
        link = self.getLink(Rel.PERSON)
        if link is None or link.href == "":
            return None

        request = self.createAuthenticatedGedcomxRequest("GET", url=link.href)
        return self.stateFactory.buildPersonState(self.session, request, self.invoke(request), self.accessToken)

    def readChild(self, child):
        """

        :param Person child: Child
        :return:
        """
        link = child.getLink(Rel.PERSON)
        if link is None:
            link = child.getLink(Rel.SELF)

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
