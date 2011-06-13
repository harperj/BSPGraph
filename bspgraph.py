import loader
import bspnode

class BSPGraph:
    def __init__(self, num_nodes, step_function=None):
        self.num_nodes = num_nodes
        self.nodes = [bspnode.BSPNode(self, node_id) for node_id in xrange(num_nodes)]
        self.master_inbox = []
        if step_function != None:
            self.setStep(step_function)
    
    def initialize(self, filename):
        edges = loader.readInEdgesASCII(filename)
        self.buildGraphFromEdgeList(edges)
    
    def setStep(self, step_function):
        for node in self.nodes:
            node.setStep(step_function)
            
    def run(self):
        all_asleep = False
        while not all_asleep:
            all_asleep = True
            self.deliverMessages()
            for node in self.nodes:
                if node.active:
                    all_asleep = False
                    node.step()
        print "All nodes asleep, ending run."
        
        
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
            
    def sendMessage(self, message):
         self.master_inbox.append(message)
         
    def deliverMessages(self):
        for message in self.master_inbox:
            if self.nodes[message[0]].active == False:
                #If a node is inactive and receives a message, it should be reactivated.
                self.nodes[message[0]].active = True
                
            self.nodes[message[0]].inbox.append(message)
        self.master_inbox = []