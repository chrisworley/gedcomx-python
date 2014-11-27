# -*- coding: utf-8 -*-

from ..client import Rel
from .gedcomxapplicationstate import GedcomxApplicationState


class AgentState(GedcomxApplicationState):
    """
    AgentState:
    """

    def __init__(self, session, request, response, accessToken, stateFactory):
        super(AgentState, self).__init__(session, request, response, accessToken, stateFactory)

    def reconstruct(self, request, response):
        return AgentState(self.session, request, response, self.accessToken, self.stateFactory)

    def getAgent(self):
        """Return the agent stored in the state, if any"""
        if self.entity is not None and len(self.entity.agents) > 0:
            return self.entity.agents[0]

    def getMainDataElement(self):
        return self.getAgent()

    def getSelfRel(self):
        return Rel.AGENT