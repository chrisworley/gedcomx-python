# -*- coding: utf-8 -*-

__author__ = 'Sandeep S <codereverser@gmail.com>'
__date__ = '27-July-2014'

from .agent import Agent
from .attribution import Attribution
from .property import ListProperty
from .document import Document
from .event import Event
from .person import Person
from .placedescription import PlaceDescription
from .relationship import Relationship
from .hypermediaenableddata import HyperMediaEnabledData
from .link import Link
from .collection import Collection
from .field import Field
from .recorddescriptor import RecordDescriptor
from .sourcedescription import SourceDescription


class Gedcomx(HyperMediaEnabledData):
    """The GEDCOM X data formats define the serialization formats of the GEDCOM X conceptual model. The canonical
    documentation is provided by the formal specification documents:

    * `The GEDCOM X Conceptual Model, Version 1.0 <https://github.com/FamilySearch/gedcomx/blob/master/specifications/conceptual-model-specification.md>`_
    * `The GEDCOM X JSON Format, Version 1.0 <https://github.com/FamilySearch/gedcomx/blob/master/specifications/json-format-specification.md>`_
    * `The GEDCOM X XML Format, Version 1.0 <https://github.com/FamilySearch/gedcomx/blob/master/specifications/xml-format-specification.md>`_
    * `Link text <http://example.com/>`_

    This documentation is provided as a non-normative reference guide.

    :ivar str lang: The language of the genealogical data.
    :ivar str descriptionRef: A reference to a description of this data set.
    :ivar str profile: A reference to the profile that describes this data set.
    :ivar Attribution attribution:  The attribution of this genealogical data.
    :ivar Person[] persons:  The persons included in this genealogical data set.
    :ivar Relationship[] relationships: The relationships included in this genealogical data set.
    :ivar SourceDescription[] sourceDescriptions: The descriptions of sources included in this genealogical data set.
    :ivar Agent[] agents: The agents included in this genealogical data set.
    :ivar Event[] events: The events included in this genealogical data set.
    :ivar PlaceDescription[] places: The places included in this genealogical data set.
    :ivar Document[] documents: The documents included in this genealogical data set.
    :ivar Collection[] collections: The collections included in this genealogical data set.
    :ivar Field[] fields: The extracted fields included in this genealogical data set.
    :ivar RecordDescriptor[] recordDescriptors: The record descriptors included in this genealogical data set."""

    def __init__(self, obj=None):
        self.lang = ""
        self.description = ""
        self.profile = ""
        self.attribution = Attribution()
        self.persons = ListProperty(Person)
        self.relationships = ListProperty(Relationship)
        self.sourceDescriptions = ListProperty(SourceDescription)
        self.agents = ListProperty(Agent)
        self.events = ListProperty(Event)
        self.places = ListProperty(PlaceDescription)
        self.documents = ListProperty(Document)
        self.collections = ListProperty(Collection)
        self.fields = ListProperty(Field)
        self.recordDescriptors = ListProperty(RecordDescriptor)
        super(Gedcomx, self).__init__(obj)

    def embed(self, entity):

        for prop in self.get_list_properties():
            targets = getattr(self, prop)
            sources = getattr(entity, prop)
            for source in sources:
                for target in targets:
                    if isinstance(source, Link):
                        if source.rel == target.rel:
                            break
                    elif source.id == target.id:
                        break
                else:
                    targets.append(source)