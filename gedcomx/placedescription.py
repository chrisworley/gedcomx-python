# -*- coding: utf-8 -*-

from .property import ListProperty
from .resourcereference import ResourceReference
from .textvalue import TextValue
from .date import Date
from .placedisplayproperties import PlaceDisplayProperties
from .subject import Subject


class PlaceDescription(Subject):
    """A PlaceDescription is used to describe the details of a place in terms of its name and possibly its type,
    time period, and/or a geospatial description -- a description of a place as a snapshot in time.

    :ivar str type: An implementation-specific uniform resource identifier (URI) used to identify the type of a place
                    (e.g., address, city, county, province, state, country, etc.).
    :ivar TextValue[] names: An ordered list of standardized (or normalized), fully-qualified (in terms of what is
                             known of the applicable jurisdictional hierarchy) names for this place that are applicable
                             to this description of this place.
    :ivar Date temporalDescription: A description of the time period to which this place description is relevant.
    :ivar float latitude: Degrees north or south of the Equator.
    :ivar float longitude: Angular distance in degrees, relative to the Prime Meridian.
    :ivar ResourceReference spatialDescription: A reference to a geospatial description of this place.
    :ivar ResourceReference jurisdiction: A reference to a description of the jurisdiction this place.
    :ivar PlaceDisplayProperties display: Display properties for the place. Display properties are not
                                                   specified by GEDCOM X core, but as extension elements by GEDCOM X RS.
    """

    def __init__(self, obj=None):
        self.type = ""
        self.names = ListProperty(TextValue)
        self.temporalDescription = Date()
        self.latitude = 0.0
        self.longitude = 0.0
        self.spatialDescription = ResourceReference()
        self.jurisdiction = ResourceReference()
        self.display = PlaceDisplayProperties()
        super(PlaceDescription, self).__init__(obj)
