# -*- coding: utf-8 -*-

from .gedcomxobject import GedcomXObject


class Link(GedcomXObject):
    """ A hypermedia link, used to drive the state of a hypermedia-enabled genealogical data application.

    :ivar hreflang: The language of the resource being linked to.
    :ivar template: A URL template per http://tools.ietf.org/html/rfc6570 , used to link to a range of URIs, such as for
          the purpose of linking to a query.
    :ivar title: Human readable information about the link.
    :ivar allow: metadata about the available media type(s) of the resource being linked to.
    :ivar accept: metadata about the available media type(s) of the resource being linked to.
    :ivar rel: The link relationship.
    :ivar type: metadata about the available media type(s) of the resource being linked to.
    :ivar href: The target URI of the link.
    """
    __dictvariable__ = "rel"

    def __init__(self, obj=None):
        self.hreflang = ""
        self.template = ""
        self.title = ""
        self.allow = ""
        self.accept = ""
        self.rel = ""
        self.type = ""
        self.href = ""
        super(Link, self).__init__(obj)
