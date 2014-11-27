# -*- coding: utf-8 -*-

from .gedcomxobject import GedcomXObject


class ExtensibleData(GedcomXObject):
    """A set of data that supports extension elements.

    :ivar extensible_elements: Custom extension elements for a conclusion.
    """

    def __init__(self, obj=None):
        self.extensible_elements = []
        super(ExtensibleData, self).__init__(obj)

    def findExtensionOfType(self, classType):
        """Find extensions of the specified classType"""

        ret = []
        for element in self.extensible_elements:
            if isinstance(element, classType):
                ret.append(element)
        return ret