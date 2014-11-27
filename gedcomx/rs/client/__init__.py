# -*- coding: utf-8 -*-

from ... import gedcomx_enum

Rel = gedcomx_enum(
    SELF='self',
    NEXT='next',
    PREV='prev',
    PREVIOUS='prev',
    FIRST='first',
    LAST='last',

    AGENT='agent',
    ANCESTRY='ancestry',
    ARTIFACTS='artifacts',
    CHILDREN='children',
    CHILD_RELATIONSHIPS='child-relationships',
    CHANGE_HISTORY='change-history',
    COLLECTION='collection',
    COLLECTIONS='collections',
    CONCLUSION='conclusion',
    CONCLUSIONS='conclusions',
    CURRENT_USER_PERSON='current-user-person',
    CURRENT_USER_RESOURCES='current-user-resources',
    DESCENDANCY='descendancy',
    DESCRIPTION='description',
    EVIDENCE_REFERENCE='evidence-reference',
    EVIDENCE_REFERENCES='evidence-references',
    MEDIA_REFERENCE='media-reference',
    MEDIA_REFERENCES='media-references',
    NOTE='note',
    NOTES='notes',
    OAUTH2_AUTHORIZE='http://oauth.net/core/2.0/endpoint/authorize',
    OAUTH2_TOKEN='http://oauth.net/core/2.0/endpoint/token',
    PARENT_RELATIONSHIPS='parent-relationships',
    PARENTS='parents',
    PERSON1='person1',
    PERSON2='person2',
    PERSON='person',
    PERSONS='persons',
    PERSON_SEARCH='person-search',
    PROFILE='profile',
    RECORD='record',
    RECORDS='records',
    RELATIONSHIP='relationship',
    RELATIONSHIPS='relationships',
    SOURCE_DESCRIPTIONS='source-descriptions',
    SOURCE_REFERENCE='source-reference',
    SOURCE_REFERENCES='source-references',
    SPOUSES='spouses',
    SPOUSE_RELATIONSHIPS='spouse-relationships',
)

MEDIA_TYPES = gedcomx_enum(
    GEDCOMX_MEDIA_TYPE='application/x-gedcomx-v1+json',
    ATOM_MEDIA_TYPE='application/x-gedcomx-atom+json'
)


class GedcomxApplicationException(Exception):

    def __init__(self, message, response=None):
        self.message = message
        self.response = response
        super(GedcomxApplicationException, self).__init__(message)

