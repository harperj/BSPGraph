from collections import namedtuple

Edge = namedtuple('Edge', 'start_id, end_id, weight')

class BSPNode (object):
    def __init__(self, parent_graph, node_id, active_default = True):
        self.node_id = node_id
        self.edges = []
        self.inbox = []
        self.active = active_default
        self.parent_graph = parent_graph

    def add_edge(self, neighbor_id, weight=1):
        new_edge = Edge(self.node_id, neighbor_id, weight)
        self.edges.append(new_edge)

    def remove_duplicate_edges(self):
        #Convert the list to a set to eliminate duplicates, then convert it back
        edge_set = set(self.edges)
        self.edges = list(edge_set)

    def step(self):
        raise Exception("Undefined step function.  Subclass BSPNode to implement step().")

    def deactivate(self):
        self.active = False
