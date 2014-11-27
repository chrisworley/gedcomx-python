# -*- coding: utf-8 -*-

from ..client import Rel
from .gedcomxapplicationstate import GedcomxApplicationState


class RecordState(GedcomxApplicationState):
    """
    RecordState
    """

    def __init__(self, session, request, response, accessToken, stateFactory):
        super(RecordState, self).__init__(session, request, response, accessToken, stateFactory)

    def reconstruct(self, request, response):
        return RecordState(self.session, request, response, self.accessToken, self.stateFactory)

    def getMainDataElement(self):
        return self.entity

    def getSelfRel(self):
        return Rel.RECORD