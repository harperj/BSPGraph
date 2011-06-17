import unittest
from bspnode import *

class BSPNodeBasicTests (unittest.TestCase):
    def test_step_is_defined(self):
        #Two cases

        #1) BSPNode instantiated, step called.
        test_node = BSPNode(None, None, None)
        self.assertRaises(Exception, test_node.step, None, None, None)

        #2) BSPNode subclassed, step implemented, called.
        class TestNode (BSPNode):
            def step(self):
                pass

        test_node = TestNode(None, None, None)


    def test_add_neighbor(self):
        test_node = BSPNode(None, None, None)
        test_node.add_edge(1, 10)
        test_edge = Edge(test_node.node_id, 1, 10)
        self.assertEqual(test_node.edges[0], test_edge)

    def test_remove_duplicate_neighbors(self):
        test_node = BSPNode(None, None, None)
        test_node.add_edge(1, 3)
        test_node.add_edge(1, 3)
        test_node.add_edge(3, 5)
        test_node.add_edge(4, 2)
        test_node.add_edge(4, 2)

        #This should eliminate one of the '1' edges and one of the '4' edges.
        #this leaves expected_neighbors:

        expected_edges = [
            Edge(test_node.node_id, 1, 3),
            Edge(test_node.node_id, 3, 5),
            Edge(test_node.node_id, 4, 2)
            ]

        test_node.remove_duplicate_edges()
        for edge in test_node.edges:
            self.assertIn(edge, expected_edges)


    def test_deactivate(self):
        #Create a new BSPNode with no parent_graph or node_id.  active_default should be True
        test_node = BSPNode(None, None)
        self.assertTrue(test_node.active)
        test_node.deactivate()
        self.assertFalse(test_node.active)

if __name__ == '__main__':
    unittest.main()
