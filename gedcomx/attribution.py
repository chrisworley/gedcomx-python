# -*- coding: utf-8 -*-

from .extensibledata import ExtensibleData
from .resourcereference import ResourceReference


class Attribution(ExtensibleData):
    """Attribution for genealogical information. Attribution is used to model **who** is contributing/modifying
    information, **when** they contributed it, and **why** they are making the contribution/modification.

    :ivar ResourceReference contributor: Reference to the contributor of the attributed data.
    :ivar str modified: The modified timestamp of the attributed data.
    :ivar str changeMessage: The *change message* for the attributed data, provided by the contributor.
    """

    def __init__(self, obj=None):
        self.contributor = ResourceReference()
        self.modified = ""
        self.changeMessage = ""
        super(Attribution, self).__init__(obj)
