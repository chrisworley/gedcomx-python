    # -*- coding: utf-8 -*-

__author__ = 'Sandeep S <codereverser@gmail.com>'
__version__ = '0.1'
__date__ = '02-July-2014'


from .citationfield import CitationField
from .property import ListProperty, DictProperty
from .resourcereference import ResourceReference
from .hypermediaenableddata import HyperMediaEnabledData

class SourceCitation(HyperMediaEnabledData):
    """

    :ivar str lang: The language of the note.
    :ivar ResourceReference citationTemplate: A reference to the citation template for this citation.
    :ivar CitationField[] fields: The list of citation fields.
    :ivar str value: A rendering (as a string) of the source citation.
    """

    def __init__(self, obj=None):
        self.lang = ""
        self.citationTemplate = ResourceReference()
        self.fields = DictProperty(CitationField)
        self.value = ""
        super(SourceCitation, self).__init__(obj)
