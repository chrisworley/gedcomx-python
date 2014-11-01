# -*- coding: utf-8 -*-

__author__ = 'Sandeep S <codereverser@gmail.com>'
__version__ = '0.1'
__date__ = '02-July-2014'


from .extensibledata import ExtensibleData
from .property import ListProperty
from .textvalue import TextValue
from .field import Field


class PlaceReference(ExtensibleData):
    """
    A reference to genealogical place.

    :ivar str descriptionRef: A reference to a description of the place being referenced.
    :ivar str original: The original value as supplied by the user.
    :ivar TextValue[] normalizedExtensions: The list of normalized values for the date, provided for display purposes
                                            by the application. Normalized values are not specified by GEDCOM X core,
                                            but as extension elements by GEDCOM X RS.
    :ivar Field[] fields:  The references to the record fields being used as evidence.
    """

    def __init__(self, obj=None):
        self.description = ""
        self.original = ""
        self.normalizedExtensions = ListProperty(TextValue)
        self.fields = ListProperty(Field)
        super(PlaceReference, self).__init__(obj)
