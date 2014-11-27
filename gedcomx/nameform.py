# -*- coding: utf-8 -*-

from .extensibledata import ExtensibleData
from .property import ListProperty
from .field import Field
from .namepart import NamePart


class NameForm(ExtensibleData):
    """A form of a name.

    :ivar str lang: The language of the conclusion.
    :ivar str fullText: The full text of the name form.
    :ivar NamePart[] parts: The different parts of the name form.
    :ivar Field[] fields: The references to the record fields being used as evidence."""

    def __init__(self, obj=None):
        self.lang = ""
        self.fullText = ""
        self.parts = ListProperty(NamePart)
        self.fields = ListProperty(Field)
        if isinstance(obj, (str, unicode)):
            self.fullText = obj
            super(NameForm, self).__init__()
        else:
            super(NameForm, self).__init__(obj)