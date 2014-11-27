# -*- coding: utf-8 -*-

from .address import Address
from .hypermediaenableddata import HyperMediaEnabledData
from .identifier import Identifier
from .property import ListProperty, DictProperty
from .onlineaccount import OnlineAccount
from .resourcereference import ResourceReference
from .textvalue import TextValue


class Agent(HyperMediaEnabledData):
    """An agent, e.g. person, organization, or group. In genealogical research, an agent often
    takes the role of a contributor.

    :ivar OnlineAccount[] accounts: The accounts that belong to this person or organization.
    :ivar Address[] addresses: The addresses that belong to this person or organization.
    :ivar ResourceReference[] emails: The emails that belong to this agent.
    :ivar ResourceReference homepage: The homepage.
    :ivar identifiers: The list of identifiers for the agent.
    :ivar TextValue[] names: The list of names for this agent.
    :ivar openid: The openid of the person or organization.
    :ivar phones: The phones that belong to this agent.
    """

    def __init__(self, obj=None):
        self.accounts = ListProperty(OnlineAccount)
        self.addresses = ListProperty(Address)
        self.emails = ListProperty(ResourceReference)
        self.homepage = ResourceReference()
        self.identifiers = DictProperty(Identifier)
        self.names = ListProperty(TextValue)
        self.openid = ResourceReference()
        self.phones = ListProperty(ResourceReference)
        super(Agent, self).__init__(obj)

    def name(self, name):
        self.names.append( name )

    def email(self, email):
        self.emails.append( ResourceReference('mailto:' + email) )