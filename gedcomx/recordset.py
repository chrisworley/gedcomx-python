# -*- coding: utf-8 -*-

__author__ = 'Sandeep S <codereverser@gmail.com>'
__date__ = '03-July-2014'

from .hypermediaenableddata import HyperMediaEnabledData


class RecordSet(HyperMediaEnabledData):
    """The GEDCOM X bulk record data formats are used to exchange bulk genealogical data sets, grouped into records.

    :ivar str lang: The language of the genealogical data.
    :ivar Gedcomx metadata: Metadata about this record set; shared among all records in the set.
    :ivar Gedcomx[] records: The records included in this genealogical data set."""

    def __init__(self, obj=None):
        self.lang = ""
        self.metadata = None
        self.records = []
        super(RecordSet, self).__init__(obj)