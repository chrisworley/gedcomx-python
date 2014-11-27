# -*- coding: utf-8 -*-

from .property import ListProperty
from .textvalue import TextValue
from .hypermediaenableddata import HyperMediaEnabledData
from .fieldvaluedescriptor import FieldValueDescriptor


class FieldDescriptor(HyperMediaEnabledData):
    """A description of a field in a record.

    :ivar str originalLabel: The original label for the field, as stated on the original record.
    :ivar TextValue[] description: The description of the field.
    :ivar FieldValueDescriptor[] values: Descriptors of the values that are applicable to the field."""

    def __init__(self, obj=None):
        self.originalLabel = ""
        self.description = ListProperty(TextValue)
        self.values = ListProperty(FieldValueDescriptor)
        super(FieldDescriptor, self).__init__(obj)