# -*- coding: utf-8 -*-

__author__ = 'Sandeep S <codereverser@gmail.com>'
__date__ = '02-July-2014'


from .attribution import Attribution
from .property import ListProperty
from .hypermediaenableddata import HyperMediaEnabledData
from .collectioncontent import CollectionContent


class Collection(HyperMediaEnabledData):
    """A collection of genealogical resources.

    :ivar str lang: The language of this description of the collection
    :ivar str title: A title for the collection.
    :ivar int size: The size of the collection, in terms of the number of items in this collection.
    :ivar CollectionContent[] content: Descriptions of the content of this collection.
    :ivar Attribution attribution: Attribution metadata for this collection."""

    def __init__(self, obj=None):
        self.lang = ""
        self.title = ""
        self.size = 0
        self.content = ListProperty(CollectionContent)
        self.attribution = Attribution()
        super(Collection, self).__init__(obj)
