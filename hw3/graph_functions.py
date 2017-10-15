# Charles Hong (csh6cw)
# 09/05/17
# graph_functions.py
__author__ = 'csh6cw'

from graph import Graph


# Checks if a given Graph is considered to be complete: returns an error if the argument is not a Graph
def is_complete(grph):
    if not isinstance(grph, Graph):
        raise TypeError('Please enter a Graph object!')
    else:
        if grph.num_nodes() == 1 or grph.num_nodes() == 0:
            return True
        for element in grph.dict.keys():
            if not len(grph.dict[element]) == grph.num_nodes() - 1:
                return False
        return True


# Returns a list of tuples of each node's degree in decreasing order, with the highest degree node coming first
def nodes_by_degree(grph):
    if not isinstance(grph, Graph):
        raise TypeError('Please enter a Graph object!')
    else:
        node_degrees = []
        for key, value in grph.dict.items():
            new_tuple = (str(key), len(value))
            node_degrees.append(new_tuple)
        node_degrees = sorted(node_degrees, key=lambda tup: tup[1], reverse=True)
        return node_degrees


if __name__ == '__main__':
    pass
