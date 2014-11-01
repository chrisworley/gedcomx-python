# -*- coding: utf-8 -*-

__author__ = 'Sandeep S <codereverser@gmail.com>'
__version__ = '0.1'
__date__ = '02-July-2014'

from .property import ListProperty
from .date import Date
from .eventrole import EventRole
from .placereference import PlaceReference
from .subject import Subject


class Event(Subject):
    """A historical event.

    :ivar str type: The type of the event.
    :ivar Date date: The date of the event.
    :ivar PlaceReference place: The place of the event.
    :ivar EventRole[] roles: The roles played in the event."""

    def __init__(self, obj=None):
        self.type = ""
        self.date = Date()
        self.place = PlaceReference()
        self.roles = ListProperty(EventRole)
        super(Event, self).__init__(obj)