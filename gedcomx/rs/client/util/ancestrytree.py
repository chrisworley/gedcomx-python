# -*- coding: utf-8 -*-

__author__ = 'Sandeep S <codereverser@gmail.com>'
__date__ = '16-July-2014'


class AncestryNode:

    def __init__(self, number, parent=None):
        self.number = number
        self.parent = parent

    def getPerson(self):
        """

        :return: Person
        :rtype: gedcomx.conclusion.person.Person
        """
        if self.parent is None:
            return None
        elif len(self.parent.ancestry) >= self.number:
            return self.parent.ancestry[self.number-1]

    def getFather(self):
        if self.parent is None or len(self.parent.ancestry) < self.number:
            return None
        else:
            return AncestryNode(2*self.number, parent=self.parent)

    def getMother(self):
        if self.parent is None or len(self.parent.ancestry) < self.number:
            return None
        else:
            return AncestryNode(2 * self.number + 1, parent=self.parent)


class AncestryTree:
    """AncestryTree to store the ancestry graph for  a given person.

    Note:- Each person element provides "display properties" that describe how to display the person. The display properties
    include, among other things, an ascendancyNumber which indicates the person's position in the ancestry graph using
    an Ahnen number."""

    def __init__(self, gx):
        """

        :param Gedcomx gx: The person object for which the tree is to be generated
        :return:
        """
        self.ancestry = self.buildTree(gx)

    def buildTree(self, gx):
        ancestry = []
        for person in gx.persons:
            ascendancyNumber = person.display.ascendancyNumber
            try:
                number = int(ascendancyNumber)
                while len(ancestry) < number:
                    ancestry.append(None)
                ancestry[number-1] = person
            except ValueError:
                print "Error parsing ascendancy Number: Got %s" % ascendancyNumber

        return ancestry

    def getRoot(self):
        return self.getAncestor(1)

    def getAncestor(self, number):
        if len(self.ancestry) < number:
            return None
        else:
            return AncestryNode(number, parent=self)
