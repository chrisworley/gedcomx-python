# -*- coding: utf-8 -*-

import json
from ...gedcomx import Gedcomx
from ..client import Rel
from .gedcomxapplicationstate import GedcomxApplicationState
from .personstate import PersonState


class RecordsState(GedcomxApplicationState):

    def __init__(self, session, request, response, access_token, state_factory):
        super(RecordsState, self).__init__(session, request, response, access_token, state_factory)

    def reconstruct(self, request, response):
        return RecordsState(self.session, request, response, self.accessToken, self.stateFactory)


    def getMainDataElement(self):
        return self.entity

