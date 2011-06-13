import loader
import bspnode

class BSPGraph:
    def __init__(self, num_nodes, step_function=None):
        self.num_nodes = num_nodes
        self.nodes = [bspnode.BSPNode(node_id) for node_id in xrange(num_nodes)]
        if step_function != None:
            self.setStep(step_function)
    
    def initialize(self, filename):
        edges = loader.readInEdgesASCII(filename)
        self.buildGraphFromEdgeList(edges)
    
    def setStep(self, step_function):
        for node in self.nodes:
            node.setStep(step_function)
        
    def addUndirectedEdge(self, start, end, weight=1):
        self.nodes[start].addNeighbor(end)
        self.nodes[end].addNeighbor(start)
        
    def buildGraphFromEdgeList(self, edge_list):
        for edge in edge_list:
            self.addUndirectedEdge(edge[0], edge[1])
        self.removeDuplicateNeighbors()
        
    def removeDuplicateNeighbors(self):
        for node in self.nodes:
            node.removeDuplicateNeighbors()