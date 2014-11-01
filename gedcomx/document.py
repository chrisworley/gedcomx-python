# -*- coding: utf-8 -*-

__author__ = 'Sandeep S <codereverser@gmail.com>'
__version__ = '0.1'
__date__ = '02-July-2014'


from .conclusion import Conclusion


class Document(Conclusion):
    """An abstract document that contains derived (conclusionary) text -- for example, a transcription
    or researcher analysis.

    :ivar str textType: The text type of the document.
    :ivar bool extracted: Whether this document is identified as _extracted_.
    :ivar str type: The type of the document.
    :ivar str text: The document text.
    """

    def __init__(self, obj=None):
        self.textType = ""
        self.extracted = False
        self.type = ""
        self.text = ""

        super(Document, self).__init__(obj)
