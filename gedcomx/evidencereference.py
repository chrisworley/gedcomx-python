# -*- coding: utf-8 -*-

from .hypermediaenableddata import HyperMediaEnabledData
from .attribution import Attribution
from .gedcomxobject import GedcomXObject

class EvidenceReference(HyperMediaEnabledData):
    """A reference to a resource that is being used as evidence.

    :ivar resourceId: The resource id of the resource being referenced.
    :ivar resource: The URI to the resource.
    :ivar attribution: Attribution metadata from the evidence reference.
    """

    def __init__(self, obj=None):
        self.resourceId = ""
        self.resource = ""
        self.attribution = Attribution()
        if isinstance(obj, GedcomXObject):
            self.resource = '#' + obj.id
            super(EvidenceReference, self).__init__()
        else:
            super(EvidenceReference, self).__init__(obj)

    def setReference(self, gx):
        self.resource = '#' + gx.id
