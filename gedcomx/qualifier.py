# -*- coding: utf-8 -*-

__author__ = 'Sandeep S <codereverser@gmail.com>'
__version__ = '0.1'
__date__ = '02-July-2014'

from .baseobject import BaseObject


class Qualifier(BaseObject):
    """ A data qualifier. Qualifiers are used to "qualify" certain data elements to provide additional context,
    information, or details.

    :ivar name: The name of the qualifier.
    :ivar value: The value of the qualifier."""


    def __init__(self, obj=None):
        self.name = ""
        self.value = ""

        super(Qualifier, self).__init__(obj)

