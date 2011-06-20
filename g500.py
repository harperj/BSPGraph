from bspgraph import *
from bspnode import *

class BFSGraph (BSPGraph):
    def pick_target(self):
        import random
        target_node_edges = 0
        target_node = -1
        while target_node_edges == 0:
            target_node = random.randint(0, self.num_nodes-1)
            target_node_edges = len(self.nodes[target_node].edges)
        return target_node

class BFSNode (BSPNode):
    def step(self):
        self.deactivate()
        if self.data != -1:
            return

        sender = -1

        if not self.inbox:
            if self.node_id == self.target_id:
                self.data = self.target_id
            else:
                return
        else:
            sender = self.inbox[0].data
            self.data = sender
            self.inbox = []

        for edge in self.edges:
            self.parent_graph.send_message(Message(edge.end_id, self.node_id))
