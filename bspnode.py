class BSPNode:
    def __init__(self, parent_graph, node_id, active_default = True):
        self.node_id = node_id
        self.neighbors = []
        self.inbox = []
        self.active = active_default
        self.parent_graph = parent_graph
        
    def addNeighbor(self, neighbor_id):
        self.neighbors.append(neighbor_id)
        
    def removeDuplicateNeighbors(self):
        #Convert the list to a set to eliminate duplicates, then convert it back
        neighbor_set = set(self.neighbors)
        self.neighbors = list(neighbor_set)
        
    def step(self):
        self.step_function(self)
        
    def setStep(self, step_function):
        self.step_function = step_function
        
    def deactivate(self):
        self.active = False