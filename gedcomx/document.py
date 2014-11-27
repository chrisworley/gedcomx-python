# -*- coding: utf-8 -*-

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
