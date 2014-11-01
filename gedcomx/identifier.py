# -*- coding: utf-8 -*-

__author__ = 'Sandeep S <codereverser@gmail.com>'
__version__ = '0.1'
__date__ = '02-July-2014'

from .baseobject import BaseObject


class Identifier(BaseObject):
    """
    An identifier for a resource.

    :ivar str type: The type of the id.
    :ivar str value: The id value.
    """

    def __init__(self, obj=None):
        self.type = ""
        self.value = ""
        super(Identifier, self).__init__(obj)

