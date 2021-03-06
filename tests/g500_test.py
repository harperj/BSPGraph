import unittest
from g500 import *
import bspgraph
import loader

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

        #Two tests: make sure there are no loops
        for node in test_graph.nodes:
            node.visiting = False
            node.checked = False
        self.loop_check(test_graph, target_id)

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

        #Now, check for loops
        for node in test_graph.nodes:
            node.visiting = False
            node.checked = False
        self.loop_check(test_graph, test_graph.target_id)

        for node in test_graph.nodes:
            if node.node_id != test_graph.target_id:
                neighbor_ids = []
                for edge in node.edges:
                    neighbor_ids.append(edge.end_id)
                self.assertIn(node.data, neighbor_ids)

    def loop_check (self, graph, node_id):
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
                    self.loop_check(graph, edge.end_id)

        node.visiting = False
        node.checked = True



class BFSGraphTests (unittest.TestCase):
    def test_initialize (self):
        test_graph = BFSGraph(256, BFSNode)
        test_graph.initialize("tests/data/4")
        edge_list = loader.readInEdgesASCII("tests/data/4")
        reverse_edges = []

        #Add the reverse of edges since these are undirected
        for edge in edge_list:
            reverse_edges.append((edge[1], edge[0]))
        for reversed_edge in reverse_edges:
            edge_list.append(reversed_edge)

        for node in test_graph.nodes:
            for edge in node.edges:
                tuple_edge = (edge.start_id, edge.end_id)
                self.assertIn(tuple_edge, edge_list)

    def test_pick_target (self):
        test_graph = BFSGraph(256, BFSNode)
        test_graph.initialize("tests/data/4")
        target = test_graph.pick_target()
        self.assertTrue(target >= 0)
        self.assertTrue(target < test_graph.num_nodes)
        #Node must have outbound edges
        self.assertNotEqual(len(test_graph.nodes[target].edges), 0)

    def test_bfs_tree_transform (self):
        class TestCompleteGraph (BFSGraph):
            def initialize (self):
                self.target_id = 0
                for node in self.nodes:
                    node.data = -1
                    node.target_id = self.target_id
                    for i in xrange(node.node_id+1, self.num_nodes):
                        self.add_undirected_edge(node.node_id, i)

        test_graph = TestCompleteGraph (15, BFSNode)
        test_graph.initialize()
        test_graph.run()
        test_graph.bfs_tree_transform()

        #This transform should turn the graph into the
        # BFS tree generated by the run()
        #Here we will check.

        for node in test_graph.nodes:
            node.visiting = False
            node.checked = False
        self.bfs_tree_check(test_graph, test_graph.target_id)

    def bfs_tree_check (self, graph, node_id):
        node = graph.nodes[node_id]
        #If we haven't finished with this node we have found
        #a loop, meaning this is not a BFS tree
        self.assertFalse(node.visiting)

        if node.checked:
            return

        node.visiting = True

        for edge in node.edges:
        #If it isn't the parent
            if node.data != edge.end_id:
                #Then assert that it MUST be a child in the BFS tree.
                #Any non-child edges should be removed in the transform.
                self.assertTrue(graph.nodes[edge.end_id].data == node.node_id)
                self.bfs_tree_check(graph, edge.end_id)

        node.visiting = False
        node.checked = True





if __name__ == '__main__':
    unittest.main()
