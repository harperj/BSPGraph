import bspgraph
import bspnode

class BFSNode (bspnode.BSPNode):
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
            sender = self.inbox[0]
            self.data = sender
            self.inbox = []

        for edge in self.edges:
            self.parent_graph.send_message((edge.end_id, self.node_id))
