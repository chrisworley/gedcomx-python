# -*- coding: utf-8 -*-

__author__ = 'Sandeep S <codereverser@gmail.com>'
__version__ = '0.1'
__date__ = '02-July-2014'

from .property import ListProperty
from .field import Field
from .displayproperties import DisplayProperties
from .fact import Fact
from .gender import Gender
from .name import Name
from .subject import Subject
from .nameform import NameForm


class Person(Subject):
    """
    A person.

    :ivar bool principal: Whether this person is the principal person extracted from the record.
    :ivar bool private: Whether this person has been designated for limited distribution or display.
    :ivar bool living: Living status of the person as treated by the system.
    :ivar Gender gender: The gender conclusion for the person.
    :ivar Name[] names: The name conclusions for the person.
    :ivar Fact[] facts: The fact conclusions for the person.
    :ivar Field[] fields: The references to the record fields being used as evidence.
    :ivar DisplayProperties display: Display properties for the person. Display properties are not specified
                                     by GEDCOM X core, but as extension elements by GEDCOM X RS."""

    def __init__(self, obj=None):
        self.principal = False
        self.private = False
        self.living = True
        self.gender = Gender()
        self.names = ListProperty(Name)
        self.facts = ListProperty(Fact)
        self.fields = ListProperty(Field)
        self.display = DisplayProperties()
        super(Person, self).__init__(obj)

    def setGender(self, genderType):
        self.gender.type = genderType

    def addFact(self, fact):
        self.facts.append(fact)

    def setName(self, name):
        if isinstance(name, Name):
            self.names.append(name)
        elif isinstance(name, (str, unicode)):
            self.names.append(Name(name))
        else:
            print("Error while setting Name")
