# -*- coding: utf-8 -*-

from .hypermediaenableddata import HyperMediaEnabledData
from .property import ListProperty
from .fieldvalue import FieldValue


class Field(HyperMediaEnabledData):
    """
    A field of a record.

    :ivar type: The type of the field.
    :ivar values: The set of values for the field.
    """

    def __init__(self, obj=None):
        self.type = ""
        self.values = ListProperty(FieldValue)

        super(Field, self).__init__(obj)

