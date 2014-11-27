# -*- coding: utf-8 -*-

from .extensibledata import ExtensibleData


class PlaceDisplayProperties(ExtensibleData):
    """A set of display properties for places for the convenience of quick display, such as for a Web-based application.
    All display properties are provided in the default locale for the current application context and are NOT considered
    canonical for the purposes of data exchange.

    :ivar str fullName: The displayable full name of the place.
    :ivar str name: The displayable name of the place.
    :ivar str type: The displayable type of the place."""

    def __init__(self, obj=None):
        self.fullName = ""
        self.name = ""
        self.type = ""
        super(PlaceDisplayProperties, self).__init__(obj)
