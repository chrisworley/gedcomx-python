# -*- coding: utf-8 -*-

from ....person import Person


class DescendancyNode:
    """
    Represents a single node in the descendancy tree.
    """

    def __init__(self):
        self.person = Person()
        self.spouse = Person()
        self.children = []

    def __str__(self):
        if len(self.person.names) > 0:
            pName = self.person.names[0].nameForms[0].fullText
        else:
            pName = ""

        if len(self.spouse.names) > 0:
            sName = self.spouse.names[0].nameForms[0].fullText
        else:
            sName = ""

        cNames = []
        for child in self.children:
            if len(child.names) > 0:
                cNames.append(child.names[0].nameForms[0].fullText)
            else:
                cNames.append("")

        return "Person - %s : Spouse - %s : Children : %s" % (pName, sName, cNames)


class DescendancyTree:
    """Computes the descendancy tree of a person"""

    def __init__(self, GedcomxObj):
        self.root = self.buildTree(GedcomxObj)

    def buildTree(self, gx):
        """
        Generates the descendency tree and returns the root node.
        :param Gedcomx gx: Object for which the tree is to be generated.
        :return: DescendancyNode
        """

        if len(gx.persons) < 0:
            return None

        root = []
        for person in gx.persons:
            number = person.display.descendancyNumber
            spouse = number.endswith("-S") or number.endswith("-s")
            if spouse:
                number = number[:-2]

            coordinates = [int(x) for x in number.split(".") if x != ""]
            current = root

            idx = 0

            while current is not None:
                coord = coordinates[idx]
                while len(current) < coord:
                    current.append(None)

                node = current[coord-1]
                if node is None:
                    current[coord-1] = DescendancyNode()
                    node = current[coord-1]

                idx += 1
                if idx < len(coordinates):
                    children = node.children
                    current = children
                else:
                    current = None

            if spouse:
                node.spouse = person
            else:
                node.person = person

        if len(root) > 0:
            return root[0]
        else:
            return None

    def printTree(self, node=0):
        if node == 0:
            node = self.root
        if node is None:
            return
        print node
        for child in node.children:
            self.printTree(child)