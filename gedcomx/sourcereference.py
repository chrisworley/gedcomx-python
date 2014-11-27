# -*- coding: utf-8 -*-

from .attribution import Attribution
from .property import ListProperty
from .qualifier import Qualifier
from .hypermediaenableddata import HyperMediaEnabledData
from .gedcomxobject import GedcomXObject

class SourceReference(HyperMediaEnabledData):
    """
    An attributable reference to a description of a source.

    :ivar description: A reference to the description of the source being refrenced.
    :ivar attribution: The attribution metadata for this source reference.
    :ivar qualifiers: The qualifiers associated with this source reference.
    """

    def __init__(self, obj=None):
        self.description = ""
        self.attribution = Attribution()
        self.qualifiers = ListProperty(Qualifier)
        if isinstance(obj, GedcomXObject):
            self.description = u'#' + obj.id
            super(SourceReference, self).__init__()
        else:
            super(SourceReference, self).__init__(obj)

