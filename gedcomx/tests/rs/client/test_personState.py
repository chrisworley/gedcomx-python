# -*- coding: utf-8 -*-

__author__ = 'Sandeep S <codereverser@gmail.com>'
__date__ = '06-July-2014'

import unittest

from ....gedcomx import Gedcomx
from ....property import ListProperty
from ....person import Person
from ....rs.client import Rel
from ....rs.client.statefactory import StateFactory
from ....rs.client.personstate import PersonState
from ....types import GenderType, NamePartType


class TestPersonState(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.stateFactory = StateFactory()
        state = cls.stateFactory.newPersonState("https://sandbox.familysearch.org/.well-known/app-meta")
        state.authenticateViaOAuth2Password("tuf000205040", "1234pass",
                                                      "WCQY-7J1Q-GKVV-7DNM-SQ5M-9Q5H-JX3H-CMJK")
        cls.personState = state.readPersonForCurrentUser()
        cls.personState.loadEmbeddedResources()

    def test_constructor(self):
        self.assertIsInstance(self.personState, PersonState,
                                     "Expected PersonState class. Got %s" % type(self.personState))
    # def test_reconstruct(self):
    #     self.fail()
    #

    def test_getScope(self):
        self.assertIsNotNone(self.personState.getScope())
        self.assertIsInstance(self.personState.getScope(), Gedcomx)

    # def test_getMainDataElement(self):
    #     self.fail()
    #
    #
    def test_getLocalId(self):
        self.assertEqual(self.personState.getLocalId(), "KWWM-TWV")

    def test_getPerson(self):
        self.assertIsInstance(self.personState.getPerson(), Person)

    def test_getRelationships(self):
        relations = self.personState.getRelationships()
        self.assertIsInstance(relations, ListProperty)
        self.assertEqual(len(relations), 3) # 2 ParentChild + 1 Couple; May change later when children and sibling relations are added.

    def test_getSpouseRelationShips(self):
        spouse_relations = self.personState.getSpouseRelationShips()
        self.assertEqual(len(spouse_relations), 1)

    #
    # def test_getChildRelationShips(self):
    #     self.fail()
    #
    # def test_getParentRelationShips(self):
    #     self.fail()
    #
    # def test_getDisplayProperties(self):
    #     self.fail()
    #
    # def test_getName(self):
    #    self.personState.getName()

    def test_getGender(self):
         self.assertIsNotNone(self.personState.getGender())
         self.assertEqual(self.personState.getGender().type, GenderType.Female)

    def test_updateName(self):
        name = self.personState.getName()
        nameform = name.nameForms[0]
        nameform.fullText = "Meredith Brown"
        for part in nameform.parts:
            if part.type == NamePartType.Given:
                part.value = "Meredith"
            elif part.type == NamePartType.Surname:
                part.value = "Brown"
        returnstate = self.personState.updateProperties(self.personState.getPerson(), Rel.CONCLUSIONS)
        self.assertTrue(returnstate.ifSuccessful())
    #
    # def test_getFact(self):
    #     self.fail()
    #
    # def test_getConclusion(self):
    #     self.fail()
    #
    # def test_getNote(self):
    #     self.fail()
    #
    # def test_getSourceReference(self):
    #     self.fail()
    #
    # def test_getEvidenceReference(self):
    #     self.fail()
    #
    # def test_getPersonalReference(self):
    #     self.fail()
    #
    # def test_getMediaReference(self):
    #     self.fail()
    #
    # def test_readCollection(self):
    #     self.fail()
    #
    def test_readAncestry(self):
        state = self.personState.readAncestry()
        tree = state.getTree()
        self.assertIsNotNone(tree)
        self.assertEqual(len(tree.ancestry), 3)

    def test_readDescendancy(self):
        state = self.personState.readDescendancy()
        tree = state.getTree()
        self.assertIsNotNone(tree)
        tree.printTree()

    # def test_createEmptySelf(self):
    #     self.fail()
    #
    # def test_update(self):
    #     self.fail()
    #
    # def test_addGender(self):
    #     self.fail()
    #
    # def test_addName(self):
    #     self.fail()
    #
    # def test_addNames(self):
    #     self.fail()
    #
    # def test_addFact(self):
    #     self.fail()
    #
    # def test_addFacts(self):
    #     self.fail()
    #
    # def test_updateProperties(self):
    #     self.fail()
    #
    # def test_deleteProperty(self):
    #     self.fail()
    #
    # def test_readProperty(self):
    #     self.fail()
    #
    # def test_updateConclusions(self):
    #     self.fail()
    #
    # def test_deleteName(self):
    #     self.fail()
    #
    # def test_deleteGender(self):
    #     self.fail()
    #
    # def test_deleteFact(self):
    #     self.fail()
    #
    # def test_deleteConclusion(self):
    #     self.fail()
    #
    # def test_addSourceReference(self):
    #     self.fail()
    #
    # def test_addSourceReferences(self):
    #     self.fail()
    #
    # def test_updateSourceReferences(self):
    #     self.fail()
    #
    # def test_deleteSourceReference(self):
    #     self.fail()
    #
    # def test_addMediaReference(self):
    #     self.fail()
    #
    # def test_addMediaReferences(self):
    #     self.fail()
    #
    # def test_updateMediaReferences(self):
    #     self.fail()
    #
    # def test_deleteMediaReference(self):
    #     self.fail()
    #
    # def test_addEvidenceReference(self):
    #     self.fail()
    #
    # def test_addEvidenceReferences(self):
    #     self.fail()
    #
    # def test_updateEvidenceReferences(self):
    #     self.fail()
    #
    # def test_deleteEvidenceReference(self):
    #     self.fail()
    #
    # def test_addPersonalReference(self):
    #     self.fail()
    #
    # def test_addPersonalReferences(self):
    #     self.fail()
    #
    # def test_updatePersonalReferences(self):
    #     self.fail()
    #
    # def test_deletePersonalReference(self):
    #     self.fail()
    #
    # def test_readNote(self):
    #     self.fail()
    #
    # def test_addNote(self):
    #     self.fail()
    #
    # def test_addNotes(self):
    #     self.fail()
    #
    # def test_updateNotes(self):
    #     self.fail()
    #
    # def test_deleteNote(self):
    #     self.fail()
    #
    # def test_readRelationShip(self):
    #     self.fail()
    #
    # def test_readRelative(self):
    #     self.fail()
    #
    # def test_readSpouseByRelationship(self):
    #     self.fail()
    #
    # def test_readSpouseById(self):
    #     self.fail()
    #
    def test_readSpouse(self):
        state = self.personState.readSpouse(0)
        self.assertIsNotNone(state)
        desc_state = state.readDescendancy()
        self.assertIsNotNone(desc_state)
        tree = desc_state.getTree()
        self.assertIsNotNone(tree)
        tree.printTree()
    #
    # def test_readSpouses(self):
    #     self.fail()
    #
    # def test_addSpouse(self):
    #     self.fail()
    #

if __name__ == "__main__":
    unittest.main()