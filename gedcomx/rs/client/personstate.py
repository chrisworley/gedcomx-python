# -*- coding: utf-8 -*-

__author__ = 'Sandeep S <codereverser@gmail.com>'
__version__ = '0.1'
__date__ = '03-July-2014'

import json

from ...property import ListProperty
from ...relationship import Relationship
from ...person import Person
from ...types import RelationshipType
from .gedcomxapplicationstate import GedcomxApplicationState
from ..client import Rel, GedcomxApplicationException
from ...gedcomx import Gedcomx


class PersonState(GedcomxApplicationState):
    """

    """

    def __init__(self, session, request, response, access_token, state_factory):
        super(PersonState, self).__init__(session, request, response, access_token, state_factory)

    def reconstruct(self, request, response):
        return PersonState(self.session, request, response, self.accessToken, self.stateFactory)

    def getScope(self):
        return self.entity

    def getMainDataElement(self):
        return self.getPerson()

    def getSelfRel(self):
        return Rel.PERSON

    def getLocalId(self):
        person = self.getPerson()
        if person is not None:
            return person.id
        else:
            return ""

    def refersToMe(self, ref):
        """ Whether the resource `ref` refers to the current object

        :param ResourceReference ref: The resource reference to be checked against.
        :return: True or False
        """
        return ref is not None and ref.resource.endswith(self.getLocalId())

    def getPerson(self):
        """ Returns the first person referenced by this object.

        :return:
        :rtype: Person
        """
        if self.entity is not None and len(self.entity.persons) > 0:
            return self.entity.persons[0]

    def getPersons(self):
        if self.entity is not None:
            return self.entity.persons
        else:
            return None

    def getRelationships(self):
        if self.entity is not None:
            return self.entity.relationships
        else:
            return None

    def getSpouseRelationShips(self):
        relationships = self.getRelationships()
        if relationships is None:
            return None
        srelationships = ListProperty(Relationship)
        for relationship in relationships:
            if relationship.type == RelationshipType.Couple:
                srelationships.append(relationship)
        return srelationships

    def getChildRelationShips(self):
        relationships = self.getRelationships()
        if relationships is None:
            return None
        srelationships = ListProperty(Relationship)
        for relationship in relationships:
            if relationship.type == RelationshipType.ParentChild and self.refersToMe(relationship.person1):
                srelationships.append(relationship)
        return srelationships

    def getParentRelationShips(self):
        relationships = self.getRelationships()
        if relationships is None:
            return None
        srelationships = ListProperty(Relationship)
        for relationship in relationships:
            if relationship.type == RelationshipType.ParentChild and self.refersToMe(relationship.person2):
                srelationships.append(relationship)
        return srelationships

    def getDisplayProperties(self):
        person = self.getPerson()
        if person is None:
            return None
        else:
            return person.display

    def getName(self):
        person = self.getPerson()
        if person is not None and len(person.names) > 0:
            return person.names[0]

    def getGender(self):
        person = self.getPerson()
        if person is not None:
            return person.gender

    def getFact(self):
        person = self.getPerson()
        if person is not None and len(person.facts) > 0:
            return person.facts[0]

    def getConclusion(self):
        return self.getName() or self.getGender() or self.getFact()

    def getNote(self):
        person = self.getPerson()
        if person is not None and len(person.notes) > 0:
            return person.notes[0]

    def getSourceReference(self):
        person = self.getPerson()
        if person is not None and len(person.sources) > 0:
            return person.sources[0]

    def getEvidenceReference(self):
        person = self.getPerson()
        if person is not None and len(person.evidence) > 0:
            return person.evidence[0]

    def getPersonalReference(self):
        return self.getEvidenceReference()

    def getMediaReference(self):
        person = self.getPerson()
        if person is not None and len(person.media) > 0:
            return person.media[0]

    def readCollection(self):
        link = self.getLink(Rel.COLLECTION)
        if link is None or link.href == "":
            return None

        request = self.createAuthenticatedGedcomxRequest("GET", url=link.href)
        return self.stateFactory.buildCollectionState(request, self.invoke(request), self.accessToken)

    def readAncestry(self):
        link = self.getLink(Rel.ANCESTRY)
        if link is None or link.href == "":
            return None

        request = self.createAuthenticatedGedcomxRequest("GET", url=link.href)
        return self.stateFactory.buildAncestryResultsState(self.session, request, self.invoke(request), self.accessToken)

    def readDescendancy(self):
        link = self.getLink(Rel.DESCENDANCY)
        if link is None or link.href == "":
            return None
        request = self.createAuthenticatedGedcomxRequest("GET", url=link.href)
        return self.stateFactory.buildDescendancyResultsState(self.session, request, self.invoke(request), self.accessToken)

    def createEmptySelf(self):
        person = Person()
        person.id = self.getLocalId()
        return person

    def update(self, person):
        if self.getLink(Rel.CONCLUSIONS) is not None and (len(person.names) > 0
                                                          or len(person.facts) > 0 or person.gender.type != ""):
            self.updateConclusions(person)

        if self.getLink(Rel.EVIDENCE_REFERENCES) is not None and len(person.evidence) > 0:
            self.updateEvidenceReferences(person)

        if self.getLink(Rel.MEDIA_REFERENCES) is not None and len(person.media) > 0:
            self.updateMediaReferences(person)

        if self.getLink(Rel.SOURCE_REFERENCES) is not None and len(person.sources) > 0:
            self.updateSourceReferences(person)
        if self.getLink(Rel.NOTES) is not None and len(person.notes) > 0:
            self.updateNotes(person)

        gx = Gedcomx()
        gx.persons.append(person)
        request = self.createAuthenticatedGedcomxRequest("POST", url=self.getSelfUri())
        request.data = json.dumps(gx.to_dict())
        print gx.persons
        return self.stateFactory.buildPersonState(self.session, request, self.invoke(request), self.accessToken)

    def addGender(self, gender):
        person = self.createEmptySelf()
        person.gender = gender
        return self.updateConclusions(person)

    def addName(self, name):
        return self.addNames([name])

    def addNames(self, names):
        person = self.createEmptySelf()
        person.names.data = names
        return self.updateConclusions(person)

    def addFact(self, fact):
        return self.addFacts(ListProperty(fact))

    def addFacts(self, facts):
        person = self.createEmptySelf()
        person.facts.data = facts
        return self.updateConclusions(person)

    def updateProperties(self, entity, relName):
        if isinstance(entity, Person):
            gx = Gedcomx()
            gx.persons.append(entity)
            entity = gx

        target = self.getSelfUri()
        link = self.getLink(relName)
        if link is not None and link.href != "":
            target = link.href

        request = self.createAuthenticatedGedcomxRequest("POST", url=target)
        request.data = json.dumps(entity.to_dict())
        return self.stateFactory.buildPersonState(self.session, request, self.invoke(request), self.accessToken)

    def deleteProperty(self, entity, relName):
        link = entity.getLink(relName)
        if link is None:
            link = entity.getLink(Rel.SELF)

        if link is None or link.href == "":
            raise GedcomxApplicationException("Property cannot be deleted: missing link.")

        request = self.createAuthenticatedGedcomxRequest("DELETE", url=link.href)
        return self.stateFactory.buildPersonState(self.session, request, self.invoke(request), self.accessToken)

    def readProperty(self, entity, relName):
        link = entity.getLink(relName)
        if link is None:
            link = entity.getLink(Rel.SELF)

        if link is None or link.href == "":
            raise GedcomxApplicationException("Property cannot be read: missing link.")

        request = self.createAuthenticatedGedcomxRequest("GET", url=link.href)
        return self.stateFactory.buildPersonState(self.session, request, self.invoke(request), self.accessToken)

    def updateConclusions(self, entity):
        return self.updateProperties(entity, Rel.CONCLUSIONS)

    def deleteName(self, name):
        return self.deleteConclusion(name)

    def deleteGender(self, gender):
        return self.deleteConclusion(gender)

    def deleteFact(self, fact):
        return self.deleteConclusion(fact)

    def deleteConclusion(self, conclusion):
        return self.deleteProperty(conclusion, Rel.CONCLUSION)

    def addSourceReference(self, source):
        return self.addSourceReferences([source])

    def addSourceReferences(self, sources):
        person = self.createEmptySelf()
        person.sources.data = sources
        return self.updateSourceReferences(person)

    def updateSourceReferences(self, person):
        return self.updateProperties(person, Rel.SOURCE_REFERNCES)

    def deleteSourceReference(self, reference):
        return self.deleteProperty(reference, Rel.SOURCE_REFERENCE)

    def addMediaReference(self, reference):
        return self.addMediaReferences([reference])

    def addMediaReferences(self, references):
        person = self.createEmptySelf()
        person.media.data = references
        return self.updateMediaReferences(person)

    def updateMediaReferences(self, person):
        self.updateProperties(person, Rel.MEDIA_REFERENCES)

    def deleteMediaReference(self, reference):
        return self.deleteProperty(reference, Rel.MEDIA_REFERENCE)

    def addEvidenceReference(self, reference):
        return self.addEvidenceReferences([reference])

    def addEvidenceReferences(self, references):
        person = self.createEmptySelf()
        person.evidence.data = references
        return self.updateEvidenceReferences(person)

    def updateEvidenceReferences(self, person):
        return self.updateProperties(person, Rel.EVIDENCE_REFERENCES)

    def deleteEvidenceReference(self, reference):
        return self.deleteProperty(reference, Rel.EVIDENCE_REFERENCE)

    def addPersonalReference(self, reference):
        return self.addPersonalReferences([reference])

    def addPersonalReferences(self, references):
        person = self.createEmptySelf()
        person.evidence.data = references
        return self.updatePersonalReferences(person)

    def updatePersonalReferences(self, person):
        return self.updateProperties(person, Rel.EVIDENCE_REFERENCES)

    def deletePersonalReference(self, reference):
        return self.deleteProperty(reference, Rel.EVIDENCE_REFERENCE)

    def readNote(self, note):
        return self.readProperty(note, Rel.NOTE)

    def addNote(self, note):
        return self.addNotes(note)

    def addNotes(self, notes):
        person = self.createEmptySelf()
        person.notes.data = notes
        return self.updateNotes(person)

    def updateNotes(self, person):
        return self.updateProperties(person, Rel.NOTES)

    def deleteNote(self, note):
        return self.deleteProperty(note, Rel.NOTE)

    def readRelationShip(self, relationship):
        return self.readProperty(relationship, Rel.RELATIONSHIP)

    def readRelative(self, relationship):
        reference = None
        if self.refersToMe(relationship.person1):
            reference = relationship.person2
        elif self.refersToMe(relationship.person2):
            reference = relationship.person1

        if reference is None or reference.resource == "":
            return None

        request = self.createAuthenticatedGedcomxRequest("GET", url=reference.resource)
        return self.stateFactory.buildPersonState(self.session, request, self.invoke(request), self.accessToken)

    def readSpouseByRelationship(self, relationship):
        return self.readRelative(relationship)

    def readSpouseById(self, index):
        spouseRelationships = self.getSpouseRelationShips()
        if len(spouseRelationships) <= index:
            return None
        return self.readSpouseByRelationship(spouseRelationships[index])

    def readSpouse(self, index):
        if isinstance(index, int):
            return self.readSpouseById(index)
        elif isinstance(index, Relationship):
            return self.readSpouseByRelationship(index)
        else:
            return None

    def readSpouses(self):
        link = self.getLink(Rel.SPOUSES)
        if link is None or link.href == "":
            return None

        request = self.createAuthenticatedGedcomxRequest("GET", url=link.href)
        return self.stateFactory.newPersonSpousesState(request, self.invoke(request), self.accessToken)

    def addSpouse(self, person):
        collection = self.readCollection()
        if collection is None or collection.hasError():
            raise GedcomxApplicationException("Unable to add relationship. collection unavailable.")
        return collection.addSpouseRelationShip(person)
