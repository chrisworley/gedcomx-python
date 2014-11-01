# -*- coding: utf-8 -*-

__author__ = 'Sandeep S <codereverser@gmail.com>'
__version__ = '0.1'
__date__ = '03-July-2014'

from ...gedcomx import Gedcomx
from ..client import Rel
from .gedcomxapplicationstate import GedcomxApplicationState
from .personstate import PersonState


class CollectionState(GedcomxApplicationState):

    def __init__(self, session, request, response, access_token, state_factory):
        super(CollectionState, self).__init__(session, request, response, access_token, state_factory)

    def reconstruct(self, request, response):
        return CollectionState(self.session, request, response, self.accessToken, self.stateFactory)


    def getMainDataElement(self):
        return self.getCollection()

    def getCollection(self):
        if self.entity is not None and len(self.entity.collections) > 0:
            return self.entity.collections[0]


