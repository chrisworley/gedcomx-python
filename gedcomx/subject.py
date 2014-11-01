# -*- coding: utf-8 -*-

__author__ = 'Sandeep S <codereverser@gmail.com>'
__version__ = '0.1'
__date__ = '02-July-2014'

from .evidencereference import EvidenceReference
from .property import ListProperty, DictProperty
from .identifier import Identifier
from .sourcereference import SourceReference
from .conclusion import Conclusion


class Subject(Conclusion):
    """The _Subject_ data type defines the abstract concept of a genealogical _subject_. A <em>subject</em> is something
     with a unique and intrinsic identity, e.g., a person, a location on the surface of the earth. We identify that
     subject in time and space using various supporting conclusions, e.g. for a person: things like name, birth date,
     age, address, etc. We aggregate these supporting <em>conclusions</em> to form an apparently-unique identity by
     which we can distinguish our <em>subject</em> from all other possible subjects.

     :ivar bool extracted: Whether this subject has been identified as _extracted_.
     :ivar EvidenceReference[] evidence: References to the evidence being referenced.
     :ivar SourceReferenace[] media: References to multimedia resources associated with this subject.
     :ivar Identifier[] identifiers: The list of identifiers for the subject."""

    def __init__(self, obj=None):
        self.extracted = False
        self.evidence = ListProperty(EvidenceReference)
        self.media = ListProperty(SourceReference)
        self.identifiers = DictProperty(Identifier)
        super(Subject, self).__init__(obj)

