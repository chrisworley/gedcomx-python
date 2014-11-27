# -*- coding: utf-8 -*-

from .attribution import Attribution
from .property import ListProperty, DictProperty
from .note import Note
from .resourcereference import ResourceReference
from .textvalue import TextValue
from .hypermediaenableddata import HyperMediaEnabledData
from .field import Field
from .coverage import Coverage
from .sourcecitation import SourceCitation
from .sourcereference import SourceReference
from .identifier import Identifier


class SourceDescription(HyperMediaEnabledData):
    """
    Represents the description of a source.

    :ivar str about: The URI (if applicable) of the actual source.
    :ivar str mediaType: Hint about the media (MIME) type of the resource being described.
    :ivar str resourceType: The type of the resource being described.
    :ivar SourceCitation[] citations: The bibliographic citations for this source.
    :ivar ResourceReference mediator: A reference to the entity that mediates access to the described source.
    :ivar SourceReference[] sources: References to any sources to which this source is related (usually applicable to
                                     sources that are derived from or contained in another source).
    :ivar ResourceReference analysis: A reference to the analysis document explaining the analysis that went into this
                                      description of the source.
    :ivar SourceReference componentOf: A reference to the source that contains this source.
    :ivar TextValue[] titles: A list of titles for this source.
    :ivar TextValue titleLabel: A label for the title of this description.
    :ivar Note[] notes: Notes about a source.
    :ivar Attribution attribution: The attribution metadata for this source description.
    :ivar str sortKey: A sort key to be used in determining the position of this source relative to other sources in the
                       same collection.
    :ivar TextValue[] description: Human-readable descriptions of the source.
    :ivar Identifier[] identifiers: The list of identifiers for the source.
    :ivar created: The date the source was created.
    :ivar modified: The date the source was last modified.
    :ivar coverage: Declarations of the coverage of the source.
    :ivar str[] rights: The rights for this source.
    :ivar Field[] fields: The fields that are applicable to the resource being described.
    :ivar ResourceReference repository: Reference to an agent describing the repository in which the source is found.
    :ivar ResourceReference descriptorRef: Reference to a descriptor of fields and type of data that can be expected to
                                           be extracted from the source.
    """

    def __init__(self, obj=None):
        self.about = ""
        self.mediaType = ""
        self.resourceType = ""
        self.citations = ListProperty(SourceCitation)
        self.mediator = ResourceReference()
        self.sources = ListProperty(SourceReference)
        self.analysis = ResourceReference()
        self.componentOf = SourceReference()
        self.titles = ListProperty(TextValue)
        self.titleLabel = TextValue
        self.notes = ListProperty(Note)
        self.attribution = Attribution()
        self.sortKey = ""
        self.descriptions = ListProperty(TextValue)
        self.identifiers = DictProperty(Identifier)
        self.created = ""
        self.modified = ""
        self.coverage = ListProperty(Coverage)
        self.rights = ListProperty(str)
        self.fields = ListProperty(Field)
        self.repository = ResourceReference()
        self.descriptor = ResourceReference()
        super(SourceDescription, self).__init__(obj)

