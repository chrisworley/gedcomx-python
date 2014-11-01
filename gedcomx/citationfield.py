# -*- coding: utf-8 -*-

__author__ = 'Sandeep S <codereverser@gmail.com>'
__version__ = '0.1'
__date__ = '02-July-2014'

from .baseobject import BaseObject


class CitationField(BaseObject):
    """Represents a citation field -- its name and value.

    :ivar str name: The citation field's name.
    :ivar str value: The citation field's value.
    """

    def __init__(self, obj=None):
        self.name = ""
        self.value = ""
        super(CitationField, self).__init__(obj)

