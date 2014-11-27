# -*- coding: utf-8 -*-

from .extensibledata import ExtensibleData
from .property import ListProperty
from .textvalue import TextValue
from .field import Field


class Date(ExtensibleData):
    """ A concluded genealogical date.

    :ivar str original: The original text as supplied by the user.
    :ivar str formal: The formal value.
    :ivar TextValue[] normalizedExtensions: The list of normalized values for the date, provided for display purposes
                                            by the application. Normalized values are not specified by GEDCOM X core,
                                            but as extension elements by GEDCOM X RS.
    :ivar Field[] fields:  The references to the record fields being used as evidence.
    """

    def __init__(self, obj=None):
        self.original = ""
        self.formal = ""
        self.normalized = ListProperty(TextValue)
        self.fields = ListProperty(Field)
        super(Date, self).__init__(obj)
