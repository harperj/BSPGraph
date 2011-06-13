class BSPNode:
    def __init__(self, node_id):
        self.id = node_id
        self.neighbors = []
        
    def addNeighbor(self, neighbor_id):
        self.neighbors.append(neighbor_id)
        
    def removeDuplicateNeighbors(self):
        #Convert the list to a set to eliminate duplicates, then convert it back
        neighbor_set = set(self.neighbors)
        self.neighbors = list(neighbor_set)
        
    def Step(self):
        self.step_function()
        
    def setStep(self, step_function):
        self.step_function = step_function