# -*- coding: utf-8 -*-

from .extensibledata import ExtensibleData
from .link import Link
from .property import DictProperty


class HyperMediaEnabledData(ExtensibleData):
    """
    A data type that supports hyper media controls. i.e. links
    The list of hypermedia links. links are not specified by GEDCOM X core, but as extension elements by GEDCOM X RS.

    :ivar links: Collections of links.
    """

    def __init__(self, obj=None):
        self.links = DictProperty(Link)
        super(HyperMediaEnabledData, self).__init__(obj)

    def getLink(self, rel):
        """Returns the link with the relation identifier.

        :param str rel: The link relation identifier
        :return:
        """
        return self.links.get(rel)