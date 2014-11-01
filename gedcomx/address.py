# -*- coding: utf-8 -*-

__author__ = 'Sandeep S <codereverser@gmail.com>'
__date__ = '02-July-2014'

from .extensibledata import ExtensibleData


class Address(ExtensibleData):
    """An address.

    :ivar str city: The city.
    :ivar str country: The country.
    :ivar str postalCode: The postal code.
    :ivar str stateOrProvince: The state or province.
    :ivar str street: The street.
    :ivar str street2: Additional street information
    :ivar str street3:
    :ivar str street4:
    :ivar str street5:
    :ivar str street6:
    :ivar str value: The value of the property.
    """

    def __init__(self, obj=None):
        self.city = ""
        self.country = ""
        self.postalCode = ""
        self.stateOrProvince = ""
        self.street = ""
        self.street2 = ""
        self.street3 = ""
        self.street4 = ""
        self.street5 = ""
        self.street6 = ""
        self.value = ""
        super(Address, self).__init__(obj)