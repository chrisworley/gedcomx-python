# -*- coding: utf-8 -*-

__author__ = 'Sandeep S <codereverser@gmail.com>'
__date__ = '03-July-2014'

from .property import ListProperty
from .hypermediaenableddata import HyperMediaEnabledData
from .fielddescriptor import FieldDescriptor


class RecordDescriptor(HyperMediaEnabledData):
    """A descriptor for a common set of records.

    :ivar str lang: The language of this record description.
    :ivar FieldDescriptor[] fields: Descriptors of the fields that are applicable to this record.
    """

    def __init__(self, obj=None):
        self.lang = ""
        self.fields = ListProperty(FieldDescriptor)
        super(RecordDescriptor, self).__init__(obj)
