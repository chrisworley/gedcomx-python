# -*- coding: utf-8 -*-

from .property import ListProperty
from .textvalue import TextValue
from .hypermediaenableddata import HyperMediaEnabledData


class FieldValueDescriptor(HyperMediaEnabledData):
    """A way a field is to be displayed to a user.

    :ivar bool optional: Whether the treatment of the field value is optional. Used to determine whether it should be
                         displayed even if the value is empty.
    :ivar str type: The type of the field value.
    :ivar str labelId: The id of the label applicable to the field value
    :ivar TextValue[] displayLabels: The labels to be used for display purposes."""

    def __init__(self, obj=None):
        self.optional = True
        self.type = ""
        self.labelId = ""
        self.labels = ListProperty(TextValue)
        super(FieldValueDescriptor, self).__init__(obj)
