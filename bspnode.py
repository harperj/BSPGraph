class BSPNode (object):
    def __init__(self, parent_graph, node_id, active_default = True):
        self.node_id = node_id
        self.neighbors = []
        self.inbox = []
        self.active = active_default
        self.parent_graph = parent_graph

        #NOTE: Within step function, no new allocation of data, no calls to non member functions
        if not callable(self.step):
            raise Exception("No step function provided.")

    def add_neighbor(self, neighbor_id, weight):
        self.neighbors.append((neighbor_id, weight))

    def remove_duplicate_neighbors(self):
        #Convert the list to a set to eliminate duplicates, then convert it back
        neighbor_set = set(self.neighbors)
        self.neighbors = list(neighbor_set)

    def step(self):
        raise Exception("Undefined step function.  Subclass BSPNode to implement step().")

    def deactivate(self):
        self.active = False
