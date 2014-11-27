# -*- coding: utf-8 -*-

from ....property import ListProperty
from ....link import Link
from .. import Rel

DEFAULT_EMBEDDED_LINK_RELS = [Rel.CHILD_RELATIONSHIPS,
                                  Rel.CONCLUSIONS,
                                  Rel.EVIDENCE_REFERENCES,
                                  Rel.MEDIA_REFERENCES,
                                  Rel.NOTES,
                                  Rel.PARENT_RELATIONSHIPS,
                                  Rel.SOURCE_REFERENCES,
                                  Rel.SPOUSE_RELATIONSHIPS]


def loadEmbeddedLinks(entity):
    """
    Collect all links embedded in an entity to multiple groups.
    :param entity:
    :return:
    """
    embeddedLinks = ListProperty(Link)
    persons = entity.persons

    for person in persons:
        for embeddedRel in DEFAULT_EMBEDDED_LINK_RELS:
            link = person.getLink(embeddedRel)
            if link is not None:
                embeddedLinks.append(link)

    relationships = entity.relationships
    for relationship in relationships:
        for embeddedRel in DEFAULT_EMBEDDED_LINK_RELS:
            link = relationship.getLink(embeddedRel)
            if link is not None:
                embeddedLinks.append(link)

    return embeddedLinks