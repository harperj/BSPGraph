import bspgraph

class RingGraph (bspgraph.BSPGraph):
    def initialize(self):
        for i in xrange(self.num_nodes):
            self.add_undirected_edge(i, (i + 1) % self.num_nodes)
            self.nodes[i].data = float(i)
