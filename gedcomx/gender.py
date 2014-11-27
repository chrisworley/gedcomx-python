# -*- coding: utf-8 -*-

from .property import ListProperty
from .field import Field
from .conclusion import Conclusion


class Gender(Conclusion):
    """A gender conclusion.

    :ivar type: The type of the gender.
    :ivar fields: The references to the record fields being used as evidence.
    """

    def __init__(self, obj=None):
        self.type = ""
        self.fields = ListProperty(Field)
        super(Gender, self).__init__(obj)