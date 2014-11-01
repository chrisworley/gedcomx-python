# -*- coding: utf-8 -*-

__author__ = 'Sandeep S <codereverser@gmail.com>'
__version__ = '0.1'
__date__ = '02-July-2014'

from .property import ListProperty
from .conclusion import Conclusion
from .date import Date
from .nameform import NameForm


class Name(Conclusion):
    """
    A name conclusion.

    :ivar str type: The type of the name.
    :ivar bool preferred: Whether the conclusion is preferred above other conclusions of the same type.
                          Useful, for example, for display purposes.
    :ivar Date date: The date the name was first applied of adopted.
    :ivar NameForm[] nameForms: Alternate forms of the name, such as the romanized form of a non-latin name."""

    def __init__(self, obj=None):
        self.type = ""
        self.preferred = False
        self.date = Date()
        self.nameForms = ListProperty(NameForm)

        if isinstance(obj, (str, unicode)):
            self.nameForms.append( NameForm(obj) )
            super(Name, self).__init__()
        else:
            super(Name, self).__init__(obj)