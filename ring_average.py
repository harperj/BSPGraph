import ringgraph

def step_func(self):
    for msg in self.inbox:
        self.data = self.data + msg[1]
    self.data = self.data / (len(self.inbox) + 1)
    self.inbox = []
    print "Node " + str(self.node_id) + ": " + str(self.data)
    for neighbor in self.neighbors:
        message = (neighbor, self.data)
        self.parent_graph.sendMessage(message)
        
myGraph = ringgraph.RingGraph(10, step_func)
myGraph.initialize()
myGraph.run()