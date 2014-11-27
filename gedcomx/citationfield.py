# -*- coding: utf-8 -*-

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

