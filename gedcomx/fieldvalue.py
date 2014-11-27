# -*- coding: utf-8 -*-

from .conclusion import Conclusion


class FieldValue(Conclusion):
    """
    An element representing a value in a record field.

    :ivar str resource: URI that resolves to the value of the field.
    :ivar str datatype: The datatype of the text value of the field.
    :ivar str type: The type of the field value.
    :ivar str labelId: The id of the label applicable to this field value.
    :ivar str text: The text value.
    """

    def __init__(self, obj=None):
        self.resource = ""
        self.datatype = ""
        self.type = ""
        self.labelId = ""
        self.text = ""
        super(FieldValue, self).__init__(obj)