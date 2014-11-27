# -*- coding: utf-8 -*-

from .hypermediaenableddata import HyperMediaEnabledData
from .attribution import Attribution
from .property import ListProperty
from .note import Note
from .resourcereference import ResourceReference
from .sourcereference import SourceReference


class Conclusion(HyperMediaEnabledData):
    """A genealogical conclusion.

    :ivar str confidence: The level of confidence the contributor has about the data.
    :ivar str lang: The language of the conclusion.
    :ivar Attribution attribution: Attribution metadata for a conclusion.
    :ivar SourceReference[] sources: he source references for a conclusion.
    :ivar ResourceReference analysis: A reference to the analysis document explaining the analysis that went into this
          conclusion.
    :ivar Note[] notes: Notes about a person.
    """

    def __init__(self, obj=None):
        self.confidence = ""
        self.lang = ""
        self.attribution = Attribution()
        self.sources = ListProperty(SourceReference)
        self.analysis = ResourceReference()
        self.notes = ListProperty(Note)
        super(Conclusion, self).__init__(obj)

    def source(self, source):
        self.sources.append(source)