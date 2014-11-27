# -*- coding: utf-8 -*-

from .extensibledata import ExtensibleData


class DisplayProperties(ExtensibleData):
    """A set of display properties for the convenience of quick display, such as for a web-based
    application. All display properties are provided in the default locale for the current
    application context and are NOT considered canonical for the purposes of data exchange.

    :ivar name: The displayable name of the person.
    :ivar gender: The displayable label for the gender of the person.
    :ivar lifespan: The displayable label for the lifespan of the person.
    :ivar birthDate: The displayable label for the birth date of the person.
    :ivar birthPlace: The displayable label for the birth place of the person.
    :ivar deathDate: The displayable label for the death date of the person.
    :ivar deathPlace: The displayable label for the death place of the person.
    :ivar marriageDate: The displayable label for the marriage date of the person.
    :ivar marriagePlace: The displayable label for the marriage place of the person.
    :ivar ascendancyNumber: The context-specific ascendancy number for the person in relation to the other persons in
                            the request. The ancestry number is defined using the Ahnentafel numbering system.
    :ivar descendencyNumber: The context-specific descendancy number for the person in relation to the other persons in
                             the request. The descendancy number is defined using the d'Aboville numbering system."""

    def __init__(self, obj=None):
        self.name = ""
        self.gender = ""
        self.lifespan = ""
        self.birthDate = ""
        self.deathDate = ""
        self.birthPlace = ""
        self.deathPlace = ""
        self.marriageDate = ""
        self.marriagePlace = ""
        self.ascendancyNumber = ""
        self.descendancyNumber = ""
        super(DisplayProperties, self).__init__(obj)