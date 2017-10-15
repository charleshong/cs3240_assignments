# Charles Hong (csh6cw)
# 09/05/17
# hw2_set.py
__author__ = 'Charles Hong'
__emailID__ = 'csh6cw'


class OurSet:
    # Default constructor for our OurSet class
    def __init__(self):
        self.values = []

    # Adds a single item into the set if it's not already in the set; returns True if successful, otherwise False
    def add(self, item):
        if item not in self.values:
            self.values.append(item)
            return True
        return False

    # Adds a single item into the set if it's not already in the set; returns True if successful, otherwise False
    def add_list(self, list):
        added = False
        if len(list) == 0:
            return True
        for item in list:
            added = self.add(item)
        return added

    # Prints a string representation of the set with < > brackets
    def __str__(self):
        if len(self.values) == 0:
            return "<>"
        set_str = "<"
        for entry in self.values:
            if entry != self.values[-1]:
                set_str += str(entry) + ", "
        set_str += str(self.values[-1]) + ">"
        return set_str

    # Returns the size of the set
    def __len__(self):
        return len(self.values)

    # Allows the code to use the keywords 'in' and 'not in'
    def __iter__(self):
        return iter(self.values)

    # Helper method that allows the '+' operation to be used between two OurSets
    def __add__(self, other):
        for item in other.values:
            if item not in self.values:
                self.values.append(item)
        return self

    # Returns a set that unions the current set with another set using __add__
    def union(self, set2):
        union_set = OurSet()
        union_set.add_list(set2)
        union_set = union_set + self
        return union_set

    # Returns a set that only contains elements shared between the current set and another set
    def intersection(self, set2):
        inter_set = OurSet()
        for item in set2:
            if item in self.values:
                inter_set.values.append(item)
        return inter_set

if __name__ == '__main__':
    pass