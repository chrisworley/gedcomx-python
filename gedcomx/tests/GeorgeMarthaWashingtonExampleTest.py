# -*- coding: utf-8 -*-

__author__ = 'Sandeep S <codereverser@gmail.com>'
__date__ = '21-July-2014'

import unittest
import os
import collections

from gedcomx import Agent, Fact, Gedcomx, Name, NameForm, NamePart, Person, PlaceDescription, Relationship
from gedcomx import SourceCitation, SourceDescription, SourceReference, TextValue
from gedcomx.types import GenderType, FactType, NamePartType


class GeorgeMarthaWashingtonExampleTest(unittest.TestCase):
    """
    Implementation of GeorgeMathaWashinctonExampleTest from https://github.com/FamilySearch/gedcomx-java/blob/master/gedcomx-model/src/test/java/org/gedcomx/examples/GeorgeMarthaWashingtonExampleTest.java
    """

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

    def testExample(self):
        """
        Creates the gedxom object in the same method as the java class and compares with the output of java program.
        GeorgeMarthaExample_java.json in the same folder as the script contains the output from the java class.
        """
        popesCreek = self.createPopesCreek()
        mountVernon = self.createMountVernon()
        chestnutGrove = self.createChestnutGrove()

        george = self.createGeorge(popesCreek, mountVernon)
        martha = self.createMartha(chestnutGrove, mountVernon)

        marriage = self.createMarriage(george, martha)
        sources = self.citeGeorgeMarthaAndMarriage(george, martha, marriage)

        contributor = self.createContributor()

        gx = Gedcomx()
        gx.persons.set([george, martha])
        gx.relationships.set([marriage])
        gx.sourceDescriptions.set(sources)
        gx.agents.set([contributor])
        gx.attribution.contributor.resource = u"#" + contributor.id

        gx.places.set([popesCreek, mountVernon, chestnutGrove])
        gx_dict = gx.to_dict()

        # Read the json output from java program and initialize a gedcomx object.
        dirname = os.path.abspath(os.path.dirname(__file__))
        java_gx = Gedcomx()
        java_gx.load( open(os.path.join(dirname, 'data', 'GeorgeMarthaExample_java.json') ))
        java_dict = java_gx.to_dict()

        # Compare both objects.
        self.assertDictEqual(gx_dict, java_dict)
        self.assertDictEqual(java_dict, gx_dict)

    def createPopesCreek(self):
        place = PlaceDescription()
        place.id = u"888"
        place.latitude = 38.192353
        place.longitude = -76.904069
        place.names.append(TextValue(u"Pope's Creek, Westmoreland, Virginia, United States"))
        return place

    def createMountVernon(self):
        place = PlaceDescription()
        place.id = u"999"
        place.latitude = 38.721144
        place.longitude = -77.109461
        place.names.append(TextValue(u"Mount Vernon, Fairfax County, Virginia, United States"))
        return place

    def createChestnutGrove(self):
        place = PlaceDescription()
        place.id = u"KKK"
        place.latitude = 37.518304
        place.longitude = -76.984148
        place.names.append(TextValue(u"Chestnut Grove, New Kent, Virginia, United States"))
        return place

    def createContributor(self):
        agent = Agent()
        agent.id = u"GGG-GGGG"
        agent.names.append(TextValue(u"Ryan Heaton"))
        return agent

    def createGeorge(self, birthPlace, deathPlace):
        """

        :param PlaceDescription birthPlace: birth place
        :param PlaceDescription deathPlace: death place
        :return:
        """
        person = Person()
        person.gender.type = GenderType.Male
        #person.setGender(GenderType.Male)


        fact = Fact()
        fact.id = u"123"
        fact.type = FactType.Birth

        fact.date.original = u"February 22, 1732"
        fact.date.formal = u"+1732-02-22"

        fact.place.original = birthPlace.names.get().value.lower()
        fact.place.description = u"#" + birthPlace.id

        person.addFact(fact)

        fact = Fact()
        fact.id = u"456"
        fact.type = FactType.Death
        fact.date.original = u"December 14, 1799"
        fact.date.formal = u"+1799-12-14T22:00:00"
        fact.place.original = deathPlace.names.get().value.lower()
        fact.place.description = u"#" + deathPlace.id
        person.addFact(fact)

        name = Name()
        nameForm = NameForm()
        nameForm.fullText = u"George Washington"
        part = NamePart()
        part.type = NamePartType.Given
        part.value = u"George"
        nameForm.parts.append(part)
        part = NamePart()
        part.type = NamePartType.Surname
        part.value = u"Washington"
        nameForm.parts.append(part)

        name.nameForms.append(nameForm)
        name.id = u"789"

        person.names.append(name)
        person.id = u"BBB-BBBB"

        return person

    def createMartha(self, birthPlace, deathPlace):
        """

        :param PlaceDescription birthPlace: birth place
        :param PlaceDescription deathPlace: death place
        :return:
        """
        person = Person()
        person.gender.type = GenderType.Male
        #person.setGender(GenderType.Male)


        fact = Fact()
        fact.id = u"321"
        fact.type = FactType.Birth

        fact.date.original = u"June 2, 1731"
        fact.date.formal = u"+1731-06-02"
        fact.place.original = birthPlace.names.get().value.lower()
        fact.place.description = u"#" + birthPlace.id

        person.addFact(fact)

        fact = Fact()
        fact.id = u"654"
        fact.type = FactType.Death
        fact.date.original = u"May 22, 1802"
        fact.date.formal = u"+1802-05-22"
        fact.place.original = deathPlace.names.get().value.lower()
        fact.place.description = u"#" + deathPlace.id
        person.addFact(fact)

        name = Name()
        nameForm = NameForm()
        nameForm.fullText = u"Martha Dandridge Custis"
        part = NamePart()
        part.type = NamePartType.Given
        part.value = u"Martha Dandridge"
        nameForm.parts.append(part)
        part = NamePart()
        part.type = NamePartType.Surname
        part.value = u"Custis"
        nameForm.parts.append(part)

        name.nameForms.append(nameForm)
        name.id = u"987"

        person.names.append(name)
        person.id = u"CCC-CCCC"

        return person


    def createMarriage(self, george, martha):
        relationship = Relationship()
        relationship.id = u"DDD-DDDD"
        relationship.person1.resource = u"#" + george.id
        relationship.person2.resource = u"#" + martha.id

        marriage = Fact()
        marriage.date.original = u"January 6, 1759"
        marriage.date.formal = u"+01-06-1759"
        marriage.place.original = u"White House Plantation"

        relationship.facts.append(marriage)

        return relationship

    def citeGeorgeMarthaAndMarriage(self, george, martha, relationship):
        georgeSource = SourceDescription()
        georgeSource.id = u"EEE-EEEE"
        georgeSource.about = u"http://en.wikipedia.org/wiki/George_washington"
        georgecite = SourceCitation()
        georgecite.value = u'"George Washington." Wikipedia, The Free Encyclopedia. Wikimedia Foundation, Inc. 24 October 2012.'
        georgeSource.citations.append(georgecite)

        marthaSource = SourceDescription()
        marthaSource.id = u"FFF-FFFF"
        marthaSource.about = u"http://en.wikipedia.org/wiki/Martha_washington"
        marthacite = SourceCitation()
        marthacite.value = u'"Martha Washington." Wikipedia, The Free Encyclopedia. Wikimedia Foundation, Inc. 24 October 2012.'
        marthaSource.citations.append(marthacite)

        ref = SourceReference()
        ref.description = u"#" + georgeSource.id
        george.sources.append(ref)


        ref = SourceReference()
        ref.description = u"#" + marthaSource.id
        martha.sources.append(ref)

        relationship.sources.append(ref)

        return [georgeSource, marthaSource]

if __name__ == "__main__":
    unittest.main()