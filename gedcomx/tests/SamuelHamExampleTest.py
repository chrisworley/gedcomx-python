# -*- coding: utf-8 -*-

__author__ = 'Sandeep S <codereverser@gmail.com>'
__date__ = '29-July-2014'

import unittest
import collections

from gedcomx import Address, Agent, Attribution, Document, EvidenceReference, Fact, Gedcomx
from gedcomx import Person, Relationship, ResourceReference, SourceCitation, SourceDescription, SourceReference, Event
from gedcomx import EventRole
from gedcomx.types import DocumentType, ResourceType, FactType, GenderType, RelationshipType, EventType, EventRoleType


class SamuelHamExampleTest(unittest.TestCase):
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

        # Jane Doe, the researcher.
        janeDoe = Agent( {'id': u"A-1",})
        janeDoe.name(u"Jane Doe")
        janeDoe.email( u"example@example.org" )


        # Lin Yee Chung cemetry
        address = Address()
        address.city = "Salt Lake City"
        address.stateOrProvince = "Utah"
        fh1 = Agent({'id': 'A-2'})
        fh1.addresses.append(address)
        fh1.name("Family History Library")

        researchAttribution = Attribution()
        researchAttribution.contributor.resource = u'#' + janeDoe.id
        researchAttribution.modified = self.parse('2014-04-25')

        recordDescription = SourceDescription({'id': u'S-1'})
        recordDescription.titles.append(u"Marriage entry for Samuel Ham and Elizabeth Spiller, Parish Register, Wilton, Somerset, England")
        recordDescription.descriptions.append(u"Marriage entry for Samuel Ham and Elizabeth in a copy of the registers of the baptisms, marriages, and burials at the church of St. George in the parish of Wilton : adjoining Taunton, in the county of Somerset from A.D. 1558 to A.D. 1837.")
        citation = SourceCitation({'value': 'Joseph Houghton Spencer, transcriber, Church of England, Parish Church of Wilton (Somerset). <cite>A copy of the registers of the baptisms, marriages, and burials at the church of St. George in the parish of Wilton : adjoining Taunton, in the county of Somerset from A.D. 1558 to A.D. 1837</cite>; Marriage entry for Samuel Ham and Elizabeth Spiller (3 November 1828), (Taunton: Barnicott, 1890), p. 224, No. 86.'})
        recordDescription.citations.append(citation)
        recordDescription.resourceType = ResourceType.PhysicalArtifact
        recordDescription.repository.resource = u'#' + fh1  .id

        transcription = Document({'id': u'D-1',
                                  'lang': u'en',
                                  'type': DocumentType.Transcription,
                                  'text': "Samuel Ham of the parish of Honiton and Elizabeth Spiller\n" +
                                          "were married this 3rd day of November 1828 by David Smith\n" +
                                          "Stone, Pl Curate,\n" +
                                          "In the Presence of\n" +
                                          "Jno Pain.\n" +
                                          "R.G. Halls.  Peggy Hammet.\n" +
                                          "No. 86."})
        transcription.source(recordDescription)


        transcriptionDescription = SourceDescription({'id': 'S-2'})
        transcriptionDescription.about = '#' + transcription.id
        transcriptionDescription.titles.append("Transcription of marriage entry for Samuel Ham and Elizabeth Spiller, Parish Register, Wilton, Somerset, England")
        transcriptionDescription.descriptions.append("Transcription of marriage entry for Samuel Ham and Elizabeth in a copy of the registers of the baptisms, marriages, and burials at the church of St. George in the parish of Wilton : adjoining Taunton, in the county of Somerset from A.D. 1558 to A.D. 1837.")
        trans_citation = SourceCitation({'value': "Joseph Houghton Spencer, transcriber, Church of England, Parish Church of Wilton (Somerset). <cite>A copy of the registers of the baptisms, marriages, and burials at the church of St. George in the parish of Wilton : adjoining Taunton, in the county of Somerset from A.D. 1558 to A.D. 1837</cite>; Marriage entry for Samuel Ham and Elizabeth Spiller (3 November 1828), (Taunton: Barnicott, 1890), p. 224, No. 86."})
        transcriptionDescription.citations.append(trans_citation)
        transcriptionDescription.resourceType = ResourceType.DigitalArtifact
        reference = SourceReference(recordDescription)
        transcriptionDescription.sources.append(reference)

        marriage = Fact()
        marriage.type = FactType.Marriage
        marriage.date.original = "3 November 1828"
        marriage.date.formal = "+1828-11-03"
        marriage.place.original = "Wilton St George, Wilton, Somerset, England"

        samsResidence = Fact()
        samsResidence.type = FactType.Residence
        samsResidence.date.original = "3 November 1828"
        samsResidence.date.formal = "+1828-11-03"
        samsResidence.place.original = "parish of Honiton, Devon, England"

        lizsResidence = Fact()
        lizsResidence.type = FactType.Residence
        lizsResidence.date.original = "3 November 1828"
        lizsResidence.date.formal = "+1828-11-03"
        lizsResidence.place.original = "parish of Wilton, Somerset, England"


        sam = Person({'id': 'P-1',
                      'extracted': True})
        sam.source(transcriptionDescription)
        sam.setName("Samuel Ham")
        sam.setGender(GenderType.Male)
        sam.addFact(samsResidence)

        liz = Person({'id': 'P-2',
                      'extracted': True})
        liz.source(transcriptionDescription)
        liz.setName("Elizabeth Spiller")
        liz.setGender(GenderType.Female)
        liz.addFact(lizsResidence)

        witness1 = Person({'id': 'P-3',
                           'extracted': True})
        witness1.source(transcriptionDescription)
        witness1.setName("Jno. Pain")

        witness2 = Person({'id': 'P-4',
                           'extracted': True})
        witness2.source(transcriptionDescription)
        witness2.setName("R.G. Halls")

        witness3 = Person({'id': 'P-5',
                           'extracted': True})
        witness3.source(transcriptionDescription)
        witness3.setName("Peggy Hammet")

        officiator = Person({'id': 'P-6',
                             'extracted': True})
        officiator.source(transcriptionDescription)
        officiator.setName("David Smith Stone")


        marriageRelationship = Relationship()
        marriageRelationship.extracted = True
        marriageRelationship.type = RelationshipType.Couple
        marriageRelationship.setPerson1(sam)
        marriageRelationship.setPerson2(liz)
        marriageRelationship.facts.append(marriage)

        marriageEvent = Event()
        marriageEvent.id = 'E-1'
        marriageEvent.type = EventType.Marriage
        marriageEvent.extracted = True
        marriageEvent.date.original = "3 November 1828"
        marriageEvent.date.formal = "+1828-11-03"
        marriageEvent.place.original = "Wilton St George, Wilton, Somerset, England"
        marriageEvent.roles.append(EventRole(EventRoleType.Principal, sam))
        marriageEvent.roles.append(EventRole(EventRoleType.Principal, liz))
        marriageEvent.roles.append(EventRole(EventRoleType.Witness, witness1))
        marriageEvent.roles.append(EventRole(EventRoleType.Witness, witness2))
        marriageEvent.roles.append(EventRole(EventRoleType.Witness, witness3))
        marriageEvent.roles.append(EventRole(EventRoleType.Official, officiator))

        analysis = Document({'id': 'D-2',
                             'text': "...Jane Doe's analysis document..."})
        samConclusion = Person({'id': 'C-1'})
        samConclusion.evidence.append(EvidenceReference(sam))
        samConclusion.analysis = ResourceReference(analysis)

        gx = Gedcomx()
        gx.agents.append(janeDoe)
        gx.agents.append(fh1)
        gx.attribution = researchAttribution
        gx.events.append(marriageEvent)
        gx.documents.append(transcription)
        gx.persons.extend([sam, liz, witness1, witness2,witness3, officiator, samConclusion])
        gx.relationships.append(marriageRelationship)
        gx.sourceDescriptions.extend([recordDescription, transcriptionDescription])
        gx.documents.append(analysis)

        gx_dict = gx.to_dict()
        # Read the json output from java program and initialize a gedcomx object.
        dirname = os.path.abspath(os.path.dirname(__file__))
        java_gx = Gedcomx()
        java_gx.load( open(os.path.join(dirname, 'data', 'SamuelHamExampleTest_java.json') ))
        java_dict = java_gx.to_dict()

        # Compare both objects.
        self.assertDictEqual(gx_dict, java_dict)
        self.assertDictEqual(java_dict, gx_dict)


if __name__ == "__main__":
    unittest.main()