# -*- coding: utf-8 -*-

from .property import ListProperty
from .resourcereference import ResourceReference
from .fact import Fact
from .field import Field
from .subject import Subject
from .person import Person


class Relationship(Subject):
    """A relationship between two or more persons.

    :ivar str type: The type of this relationship.
    :ivar ResourceReference person1: A reference to a person in the relationship. The name _person1_; is used only to
                                     distinguish it from the other person in this relationship and implies neither order
                                     nor role. When the relationship type implies direction, it goes from _person1_ to
                                     _person2_.
    :ivar ResourceReference person2: A reference to a person in the relationship. The name _person2_; is used only to
                                     distinguish it from the other person in this relationship and implies neither order
                                     nor role. When the relationship type implies direction, it goes from _person1_ to
                                     _person2_.
    :ivar Fact[] facts: The fact conclusions for the relationship.
    :ivar Field[] fields: The references to the record fields being used as evidence."""

    def __init__(self, obj=None):
        self.type = ""
        self.person1 = ResourceReference()
        self.person2 = ResourceReference()
        self.facts = ListProperty(Fact)
        self.fields = ListProperty(Field)
        super(Relationship, self).__init__(obj)

    def setPerson1(self, person):
        if isinstance(person, Person):
            self.person1.resource = '#' + person.id
        elif isinstance(person, ResourceReference):
            self.person1 = person
        else:
            raise TypeError, "Expected Type Person or ResourceReference"

    def setPerson2(self, person):
        if isinstance(person, Person):
            self.person2.resource = '#' + person.id
        elif isinstance(person, ResourceReference):
            self.person2 = person
        else:
            raise TypeError, "Expected Type Person or ResourceReference"