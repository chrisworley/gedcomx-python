# -*- coding: utf-8 -*-

import unittest
import collections

from gedcomx import Agent, Attribution, Document, EvidenceReference, Fact, Gedcomx
from gedcomx import Person, Relationship, ResourceReference, SourceCitation, SourceDescription
from gedcomx.types import ResourceType, FactType, GenderType, RelationshipType


class EmmaBocockExampleTest(unittest.TestCase):
    maxDiff = None

    def assertDictEqual(self, d1, d2, msg=None): # assertEqual uses for dicts
        for k,v1 in d1.iteritems():
            self.assertIn(k, d2, msg)
            v2 = d2[k]
            if(isinstance(v1, collections.Iterable) and
               not isinstance(v1, basestring)):
                self.assertItemsEqual(v1, v2, msg)
            else:
                self.assertEqual(v1, v2, msg)
        return True

    def parse(self, dateString):
        from dateutil import parser
        from datetime import datetime
        delta = parser.parse(dateString) - datetime.fromtimestamp(0)
        return int( delta.total_seconds() * 1000)

    def testExample(self):
        import os
        contributor = Agent( {'id': u"A-1",})
        contributor.name(u"Jane Doe")
        contributor.email( u"example@example.org" )

        repository = Agent({'id': u"A-2"})
        repository.name(u"General Registry Office, Southport")

        attribution = Attribution()
        attribution.contributor.resource = u"#" + contributor.id
        attribution.modified = self.parse("2014-03-07")

        sourceDescription = SourceDescription()
        sourceDescription.id = u"S-1"
        sourceDescription.titles.append( u"Birth Certificate of Emma Bocock, 23 July 1843, General Registry Office" )
        sourceDescription.resourceType = ResourceType.PhysicalArtifact
        citation = SourceCitation({'value': u'England, birth certificate for Emma Bocock, born 23 July 1843; citing 1843 Birth in District and Sub-district of Ecclesall-Bierlow in the County of York, 303; General Registry Office, Southport.'})
        sourceDescription.citations.append(citation)
        sourceDescription.created = self.parse("1843-07-27")
        sourceDescription.repository.resource = "#" + repository.id

        birth = Fact()
        birth.type = FactType.Birth
        birth.date.original = u"23 June 1843"
        birth.place.original = u"Broadfield Bar, Abbeydale Road, Ecclesall-Bierlow, York, England, United Kingdom"

        emma = Person()
        emma.id = u"P-1"
        emma.extracted = True
        emma.sources.append(sourceDescription)
        emma.setName(u"Emma Bocock")
        emma.setGender(GenderType.Female)
        emma.addFact(birth)

        occupation = Fact({'type': FactType.Occupation,
                           'value': u"Toll Collector"})
        father = Person({'id': u'P-2'})
        father.extracted = True
        father.sources.append(sourceDescription)
        father.setName(u"William Bocock")
        father.addFact(occupation)

        mother = Person({'id': u'P-3'})
        mother.extracted = True
        mother.sources.append(sourceDescription)
        mother.setName(u'Sarah Bocock formerly Brough')

        fatherRelationship = Relationship()
        fatherRelationship.type = RelationshipType.ParentChild
        fatherRelationship.setPerson1(father)
        fatherRelationship.setPerson2(emma)

        motherRelationship = Relationship()
        motherRelationship.type = RelationshipType.ParentChild
        motherRelationship.setPerson1(mother)
        motherRelationship.setPerson2(emma)

        analysis = Document({'id' : u'D-1',
                             'text': u"...Jane Doe's analysis document..."})
        emmaConclusion = Person({'id': u'C-1'})
        emmaReference = EvidenceReference()
        emmaReference.setReference(emma)
        emmaConclusion.evidence.append(EvidenceReference(emma))
        emmaConclusion.analysis = ResourceReference(analysis)

        gx = Gedcomx()
        gx.agents.append(contributor)
        gx.agents.append(repository)
        gx.attribution = attribution
        gx.sourceDescriptions.append(sourceDescription)
        gx.persons.extend([emma, father, mother])
        gx.relationships.extend([fatherRelationship, motherRelationship])
        gx.documents.append(analysis)
        gx.persons.append(emmaConclusion)
        gx_dict = gx.to_dict()

        # Read the json output from java program and initialize a gedcomx object.
        dirname = os.path.abspath(os.path.dirname(__file__))
        java_gx = Gedcomx()
        java_gx.load( open(os.path.join(dirname, 'data', 'EmmaBocockExample_java.json') ))
        java_dict = java_gx.to_dict()
        # Compare both objects.
        self.assertDictEqual(gx_dict, java_dict)
        self.assertDictEqual(java_dict, gx_dict)


if __name__ == "__main__":
    unittest.main()