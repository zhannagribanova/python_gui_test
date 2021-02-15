from sys import maxsize


class Group:
    def __init__(self, identifier=None, name=None):
        self.name = name
        self.identifier = identifier

    def __repr__(self):
        return "%s" % (self.name)

    def __eq__(self, other):
        return self.name == other.name

    def id_or_max(self):
        if self.identifier:
            return int(self.identifier)
        else:
            return maxsize
