# -*- coding: utf-8 -*-

from .conclusion import Conclusion
from .resourcereference import ResourceReference


class EventRole(Conclusion):
    """A role that a specific person plays in an event.

    :ivar str type: The role type.
    :ivar ResourceReference person: Reference to the person playing the role in the event.
    :ivar str details: Details about the role of the person in the event."""

    def __init__(self, obj=None, ref=None):
        self.type = ""
        self.person = ResourceReference()
        self.details = ""

        if ref is not None:
            self.type = obj
            self.person = ResourceReference(ref)
            super(EventRole, self).__init__()
        else:
            super(EventRole, self).__init__(obj)