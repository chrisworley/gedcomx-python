# -*- coding: utf-8 -*-

__author__ = 'Sandeep S <codereverser@gmail.com>'
__date__ = '04-July-2014'

from ..client import Rel
from .gedcomxapplicationstate import GedcomxApplicationState
from .util.descendancytree import DescendancyTree


class DescendancyResultsState(GedcomxApplicationState):
    """
    DescendancyResultsState:
    """

    def __init__(self, session, request, response, accessToken, stateFactory):
        super(DescendancyResultsState, self).__init__(session, request, response, accessToken, stateFactory)

    def reconstruct(self, request, response):
        return DescendancyResultsState(self.session, request, response, self.accessToken, self.stateFactory)

    def getAgent(self):
        """Return the agent stored in the state, if any"""
        if self.entity is not None and len(self.entity.agents) > 0:
            return self.entity.agents[0]

    def getMainDataElement(self):
        return self.entity

    def getSelfRel(self):
        return super(DescendancyResultsState, self).getSelfRel()

    def getTree(self):
        if self.entity:
            return DescendancyTree(self.entity)
