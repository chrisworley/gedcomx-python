# -*- coding: utf-8 -*-

from .hypermediaenableddata import HyperMediaEnabledData
from .placereference import PlaceReference
from .date import Date


class Coverage(HyperMediaEnabledData):
    """
    A description of the coverage of a resource.

    :ivar recordType: The type of record being covered.
    :ivar gemdocx.conclusion.placereference.PlaceReference spatial: Spatial coverage.
    :ivar Date temporal: Temporal coverage.
    """

    def __init__(self, obj=None):
        self.recordType = ""
        self.spatial = PlaceReference()
        self.temporal = Date()
        super(Coverage, self).__init__(obj)

