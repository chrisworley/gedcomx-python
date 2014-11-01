# -*- coding: utf-8 -*-

__author__ = 'Sandeep S <codereverser@gmail.com>'
__version__ = '0.1'
__date__ = '02-July-2014'


from .baseobject import BaseObject


class GedcomXObject(BaseObject):
    """A basic Object. Just contains ID property

    :ivar id: Id of the object"""

    def __init__(self, obj=None):
        self.id = ""
        super(GedcomXObject, self).__init__(obj)

    def getReference(self):
        return '#' + self.id