import unittest
from g500 import *

class BFSNodeTests (unittest.TestCase):
    def test_bfs_ring (self):
        class TestRingGraph (bspgraph.BSPGraph):
            def initialize(self):
                for node in self.nodes:
                    node.target_id = 0
                    node.data = -1
                    self.add_undirected_edge(node.node_id,
                                             (node.node_id + 1)
                                              % self.num_nodes)

        test_graph = TestRingGraph(10, BFSNode)
        target_id = 0
        test_graph.initialize()
        test_graph.run()

        #Two checks -- make sure there are no loops,
        def loopCheck (self, graph, node_id):
            node = graph.nodes[node_id]

            #If we haven't finished with this
            #node yet we have found a loop.
            self.assertFalse(node.visiting)

            if node.checked:
                return

            node.visiting = True

            for edge in node.edges:
                #If it isn't the parent
                if node.data != edge.end_id:
                    #if it is a child in the bfstree
                    if graph.nodes[edge.end_id].data == node.node_id:
                        loopCheck(self, graph, edge.end_id)

            node.visiting = False
            node.checked = True

        for node in test_graph.nodes:
            node.visiting = False
            node.checked = False
        loopCheck(self, test_graph, target_id)

        # and make sure every node's data (its parent)
        # is one of its neighbors
        for node in test_graph.nodes:
            if node.node_id != target_id:
                neighbor_ids = []
                for edge in node.edges:
                    neighbor_ids.append(edge.end_id)
                self.assertIn(node.data, neighbor_ids)

    def test_bfs_complete_graph (self):
        class TestCompleteGraph (bspgraph.BSPGraph):
            def initialize (self):
                for node in self.nodes:
                    node.data = -1
                    node.target_id = 0
                    for i in xrange(node.node_id+1, self.num_nodes):
                        self.add_undirected_edge(node.node_id, i)

        test_graph = TestCompleteGraph (10, BFSNode)
        test_graph.initialize()
        for first_node in test_graph.nodes:
            for second_node in test_graph.nodes:
                if first_node != second_node:
                    this_edge = Edge(first_node.node_id, second_node.node_id, 1)
                    #We want to make sure this is really a complete graph
                    self.assertIn(this_edge, first_node.edges)

        test_graph.target_id = 0
        test_graph.run()


if __name__ == '__main__':
    unittest.main()
