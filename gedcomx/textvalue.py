# -*- coding: utf-8 -*-

from .baseobject import BaseObject


class TextValue(BaseObject):
    """ An element representing a text value that may be in a specific language.

    :ivar lang: The language of the text value.
    :ivar value: The value of the text."""

    def __init__(self, obj=None):
        self.lang = ""
        self.value = ""
        if isinstance(obj, (str,unicode)):
            self.value = obj
        else:
            super(TextValue, self).__init__(obj)
