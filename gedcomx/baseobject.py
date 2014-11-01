# -*- coding: utf-8 -*-

__author__ = 'Sandeep S <codereverser@gmail.com>'
__version__ = '0.1'
__date__ = '01-July-2014'

from .property import DictProperty, ListProperty


class BaseObject(object):
    """A basic Object. Used to implement the common functions like initializing the object from server response and
    vice versa."""

    def __init__(self, obj=None):
        if isinstance(obj, dict):
            self.initialize_from_dict(obj)

    def get_variables(self):
        """
        Returns the names of variables the object contains. Used to make the json array.

        :return: List of property names the GEMDOC X object contains.
        """
        return [x for x in [v for v in dir(self) if not ( callable(getattr(self, v)) or v.startswith("__") )]]

    def get_list_properties(self):
        """
        Returns the names of list property variables in this object.
        """
        return [x for x in [v for v in dir(self) if isinstance(getattr(self, v), ListProperty)]]

    def initialize_from_dict(self, obj):
        """
        Initialize the object from a dictionary (usually decoded using json)
        """
        for var in self.get_variables():
            if var not in obj:
                continue
            prop = getattr(self, var)
            if isinstance(prop, (BaseObject, DictProperty, ListProperty)):
                prop.initialize_from_dict(obj[var])
            else:
                setattr(self, var, obj[var])

    def to_dict(self):
        """
        Converts the object to a dictionary object and returns.

        :return: the dictionary representation of the object.
        """
        ret = {}
        for var in self.get_variables():
            prop = getattr(self, var)
            if hasattr(prop, 'to_dict'):
                value = prop.to_dict()
                if value:
                    ret[var] = value
            elif prop:
                    ret[var] = prop
        return ret

    def save(self, fp):
        """
        Save gedcomx object as a JSON formatted stream to fp (a .write()-supporting file-like object).
        """
        import json
        json.dump(self.to_dict(), fp, sort_keys=True, indent=4, separators=(',', ': '))

    def load(self, fp):
        """
        Load the object saved in a gedcomx file in the current object.
        """
        import json
        obj = json.load(fp, 'ascii')
        self.initialize_from_dict(obj)

    def dump(self):
        import json
        print json.dumps(self.to_dict(), indent=4, separators=(',', ':'))