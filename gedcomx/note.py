
from .hypermediaenableddata import HyperMediaEnabledData
from .attribution import Attribution


class Note(HyperMediaEnabledData):
    """A note about a genealogical resource (e.g. conclusion or source).

    :ivar lang: The language of the note.
    :ivar subject: The subject of the note.
    :ivar text: The text of the note.
    :ivar attribution: Attribution metadata for a note.
    """

    def __init__(self, obj=None):
        self.lang = ""
        self.subject = ""
        self.text = ""
        self.attribution = Attribution()
        super(Note, self).__init__(obj)