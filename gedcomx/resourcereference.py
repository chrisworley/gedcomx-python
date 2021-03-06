# -*- coding: utf-8 -*-

from .baseobject import BaseObject
from .gedcomxobject import GedcomXObject

class ResourceReference(BaseObject):
    """ A generic reference to a resource.

    :ivar resourceId: The resource id of the resource being referenced.
    :ivar resource: The URI to the resource.
    """

    def __init__(self, obj=None):
        self.resourceId = ""
        self.resource = ""
        if isinstance(obj, GedcomXObject):
            self.resource = '#' + obj.id
            super(ResourceReference, self).__init__()
        elif isinstance(obj, (str, unicode)):
            self.resource = obj
            super(ResourceReference, self).__init__()
        else:
            super(ResourceReference, self).__init__(obj)