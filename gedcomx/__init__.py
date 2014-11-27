# -*- coding: utf-8 -*-


def gedcomx_enum(**enums):
    """
    Data type to represent enums in python 2 & 3.

    :param enums: dictionary of enums in kwargs format.
    :return:
    """
    return type("Enum", (), enums)

from .address import Address
from .agent import Agent
from .attribution import Attribution
from .baseobject import BaseObject
from .citationfield import CitationField
from .collection import Collection
from .collectioncontent import CollectionContent
from .conclusion import Conclusion
from .coverage import Coverage
from .date import Date
from .displayproperties import DisplayProperties
from .document import Document
from .event import Event
from .eventrole import EventRole
from .evidencereference import EvidenceReference
from .extensibledata import ExtensibleData
from .fact import Fact
from .field import Field
from .fielddescriptor import FieldDescriptor
from .fieldvalue import FieldValue
from .fieldvaluedescriptor import FieldValueDescriptor
from .gedcomx import Gedcomx
from .gedcomxobject import GedcomXObject
from .gender import Gender
from .hypermediaenableddata import HyperMediaEnabledData
from .identifier import Identifier
from .link import Link
from .name import Name
from .nameform import NameForm
from .namepart import NamePart
from .note import Note
from .onlineaccount import OnlineAccount
from .person import Person
from .placedescription import PlaceDescription
from .placedisplayproperties import PlaceDisplayProperties
from .placereference import PlaceReference
from .property import DictProperty, ListProperty
from .qualifier import Qualifier
from .recorddescriptor import RecordDescriptor
from .recordset import RecordSet
from .relationship import Relationship
from .resourcereference import ResourceReference
from .sourcecitation import SourceCitation
from .sourcedescription import SourceDescription
from .sourcereference import SourceReference
from .textvalue import TextValue