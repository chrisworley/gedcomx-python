# -*- coding: utf-8 -*-

__author__ = 'Sandeep S <codereverser@gmail.com>'
__version__ = '0.1'
__date__ = '02-July-2014'

from .property import ListProperty
from .qualifier import Qualifier
from .field import Field
from .conclusion import Conclusion
from .date import Date
from .placereference import PlaceReference


class Fact(Conclusion):
    """A conclusion about a fact applicable to a person or relationship.

    :ivar bool primary: Whether this fact is the primary fact of the record from which the subject was extracted.
    :ivar str type: The type of the fact.
    :ivar Date date: The date of applicability of this fact.
    :ivar PlaceReference place: The place of applicability of this fact.
    :ivar str value: The value as supplied by the user.
    :ivar Qualifier[] qualifiers: The qualifiers associated with this fact.
    :ivar Field[] fields: The references to the record fields being used as evidence."""

    def __init__(self, obj=None):
        self.primary = False
        self.type = ""
        self.date = Date()
        self.place = PlaceReference()
        self.value = ""
        self.qualifiers = ListProperty(Qualifier)
        self.fields = ListProperty(Field)

        super(Fact, self).__init__(obj)