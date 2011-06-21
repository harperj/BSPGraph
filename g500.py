from bspgraph import *
from bspnode import *
import loader

class BFSGraph (BSPGraph):
    def initialize (self, filename):
        edge_list = loader.readInEdgesASCII(filename)
        if edge_list == False:
            raise Exception("Invalid or non-existant file.")
        self.build_graph_from_edge_list(edge_list)

        self.target_id = self.pick_target()

    def pick_target(self):
        """
        Randomly choose node_id matching a node with neighbors.

        Used to choose a 'target' or initial node for the BFS.

        """

        import random
        target_node_edges = 0
        target_node = -1
        while target_node_edges == 0:
            target_node = random.randint(0, self.num_nodes-1)
            target_node_edges = len(self.nodes[target_node].edges)
        return target_node

    def bfs_tree_transform (self):
        pass

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
