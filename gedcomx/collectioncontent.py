# -*- coding: utf-8 -*-

__author__ = 'Sandeep S <codereverser@gmail.com>'
__date__ = '02-July-2014'

from .hypermediaenableddata import HyperMediaEnabledData


class CollectionContent(HyperMediaEnabledData):
    """
    A description of the content of a collection by resource type.

    :ivar float completeness: A completeness factor for this content aspect, a value between 0 and 1.
    :ivar int count: The count of the items applicable to this content aspect.
    :ivar string resourceType: The type of resource being covered in this collection."""

    def __init__(self, obj=None):
        self.completeness = 0.0
        self.count = 0
        self.resourceType = ""
        super(CollectionContent, self).__init__(obj)
