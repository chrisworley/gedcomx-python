# -*- coding: utf-8 -*-

from .extensibledata import ExtensibleData
from .property import ListProperty
from .qualifier import Qualifier
from .field import Field


class NamePart(ExtensibleData):
    """A part of a name.

    :ivar str value: The value of the name part.
    :ivar str type: The type of the name part.
    :ivar Field[] fields: The references to the record fields being used as evidence.
    :ivar Qualifier[] qualifiers: The qualifiers associated with this name part."""

    def __init__(self, obj=None):
        self.value = ""
        self.type = ""
        self.fields = ListProperty(Field)
        self.qualifiers = ListProperty(Qualifier)
        super(NamePart, self).__init__(obj)
