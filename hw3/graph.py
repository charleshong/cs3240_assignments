# Charles Hong (csh6cw)
# 09/05/17
# graph.py
__author__ = 'csh6cw'


class Graph:
    # Initializes a graph with an optional argument to take in a preexisting dictionary
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            self.dict = {}
        else:
            self.dict = graph_dict

    # Returns a list of all nodes adjacent to a given node
    def get_adjlist(self, node):
        if node in self.dict:
            return self.dict[node]
        else:
            return None

    # Returns whether a specific node is adjacent to another specific node
    def is_adjacent(self, node1, node2):
        if node1 not in self.dict or node2 not in self.dict:
            return False
        if node1 in self.dict[node2] and node2 in self.dict[node1]:
            return True
        return False

    # Returns the total number of nodes in the graph
    def num_nodes(self):
        return len(self.dict)

    # Returns the contents of the graph as a string representation of the dictionary in a Graph object
    def __str__(self):
        return str(self.dict)

    # Allows iteration through the Graph object by using keywords such as 'in' and 'not in'
    def __iter__(self):
        return iter(self.dict)

    # Returns a boolean whether a given item is contained within the Graph object
    def __contains__(self, item):
        return self.dict.__contains__(item);

    # Returns the total number of points on a Graph object
    def __len__(self):
        return len(self.dict)

    # Tries to add in a new node to the Graph only if the given node is not already in the Graph
    def add_node(self, node):
        if node in self.dict:
            return False
        else:
            self.dict[node] = []
            return True

    # Tries to connect two nodes together only if they exist in the Graph and if they're not linked already
    def link_nodes(self, node1, node2):
        if node1 not in self.dict or node2 not in self.dict:
            return False
        elif node1 in self.dict[node2] and node2 in self.dict[node1]:
            return False
        else:
            self.dict[node1].append(node2)
            self.dict[node2].append(node1)
            return True

    # Tries to disconnect two nodes only if they exist in the Graph and if they were already connected before
    def unlink_nodes(self, node1, node2):
        if node1 not in self.dict or node2 not in self.dict:
            return False
        elif node1 in self.dict[node2] and node2 in self.dict[node1]:
            self.dict[node1].remove(node2)
            self.dict[node2].remove(node1)
            return True
        else:
            return False

    # Deletes a node from the graph only if it exists in the Graph object
    def del_node(self, node):
        if node not in self.dict:
            return False
        else:
            for entry in self.dict:
                if node in self.dict[entry]:
                    self.dict[entry].remove(node)
            del self.dict[node]
            return True


if __name__ == '__main__':
    pass
