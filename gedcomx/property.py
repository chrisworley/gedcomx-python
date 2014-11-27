# -*- coding: utf-8 -*-

import collections
import unittest


class ListProperty(collections.MutableSequence):
    """Basic list to hold only items of a pre-defined data type. Kind of emulates std::vector<data_type> (C++) or
    List<data_type> java.
    """

    def __init__(self, data_type, data=None):
        """ Constructor

        :param data_type: The data type which the class holds. Eg:- int, str, Property
        :param data: could be a list of 'data_type' items or a single item.
        :raises ValueError: if data does not contains items of type 'data_type'.
        """

        self.data_type = data_type
        self.data = []

        if isinstance(data, list):
            for item in data:
                self.append(item)
        elif data is not None:
            self.append(data)

    def __delitem__(self, key):
        return self.data.__delitem__(key)

    def __getitem__(self, key):
        return self.data[key]

    def __len__(self):
        return len(self.data)

    def __setitem__(self, key, value):
        if isinstance(value, self.data_type):
            self.data[key] = value
        else:
            self.data[key] = self.data_type(value)

    def get(self):
        """Returns the first element of the container, if it is not empty. Otherwise returns a default data_type value.
        """
        if len(self.data) > 0:
            return self.data[0]
        else:
            return self.data_type()

    def insert(self, index, data):
        """Insert object before the index."""

        if isinstance(data, self.data_type):
            self.data.insert(index, data)
        else:
            self.data.insert(index, self.data_type(data))  # Try a forced conversion. Should raise exception if failed.

    def set(self, data):
        """Set the current data of current listproperty.
        :param data: <python> list of `data_type` objects.
        """
        if not isinstance(data, (list, ListProperty)):
            raise TypeError, "data should be of type list. Got %s" % str(type(data))
        for el in data:
            if not isinstance(el, self.data_type):
                raise TypeError, "data should be a list containing %s objects. Got %s" % (
                                                                                     str(self.data_type), str(type(el)))
        self.clear()
        for item in data:
            self.data.append(item)

    def clear(self):
        """ Clears the items from the container. """
        del self.data
        self.data = []

    def to_dict(self):
        ret = []
        for item in self.data:
            if hasattr(item, 'to_dict'):
                val = item.to_dict()
            else:
                val = item
            if val:
                ret.append(val)
        return ret

    def initialize_from_dict(self, obj):
        self.clear()
        self.extend(obj)


class DictProperty(collections.MutableMapping):
    """Basic dictionary to hold only items of a pre-defined data type. Same as :class:`.ListProperty` but with key
    indices."""

    def __init__(self, data_type, *args, **kwargs):
        """
        Constructor.

        :param data_type: The data type which the class holds. Eg:- int, str, Property
        :param args: Can be used to directly initialize the dictionary.
        :param kwargs: Can be used to directly initialize the dictionary.
        """
        self.data_type = data_type
        self.data = {}

        self.data.update(dict(*args, **kwargs))

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        if isinstance(value, self.data_type):
            self.data[key] = value
        else:
            #print(" Warning Expected data of type %s. Got %s. Trying forced conversion." % (str(self.data_type),
            #                                                                                str(type(value))))
            # Try a forced conversion.
            self.data[key] = self.data_type(value)

    def __delitem__(self, key):
        del self.data[key]

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

    def clear(self):
        del self.data
        self.data = {}

    def initialize_from_dict(self, obj):
        self.clear()
        self.update(obj)

    def to_dict(self):
        ret = {}
        for key, value in self.items():
            if hasattr(value, 'to_dict'):
                item = value.to_dict()
            else:
                item = value

            if item:
                ret[key] = item

        return ret

class TestListProperty(unittest.TestCase):

    def setUp(self):
        self.lp = ListProperty(int, [3, 5, 1])
        super(TestListProperty, self).setUp()

    def test_get(self):
        self.assertEqual(self.lp.get(), 3)
        self.lp.clear()
        self.assertEqual(self.lp.get(), int() )

    def test_set(self):

        self.lp.set([1, 3, 2])

        with self.assertRaises(TypeError):
            self.lp.set("A")
        with self.assertRaises(TypeError):
            self.lp.set(["A"])

        self.assertEqual(self.lp.get(), 1)

    def test_clear(self):
        self.assertEqual(len(self.lp), 3)
        self.lp.clear()
        self.assertEqual(len(self.lp), 0)

    def test_listFunctions(self):
        l1 = [2, 3]
        l2 = ListProperty(int, [1, 2])

        # Testing list extend, addition operations
        self.lp.extend(l1)
        self.lp += l2
        self.lp += l1

        self.assertEqual(len(self.lp), 9)
        self.assertEqual(self.lp[-1], 3)


        # Testing list append and index

        self.lp.append(8)
        self.assertEqual(self.lp[-1], 8)
        self.assertEqual(self.lp.index(8), len(self.lp) - 1)


if __name__ == "__main__":
    unittest.main()