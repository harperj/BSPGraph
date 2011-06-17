import unittest
from bspgraph import *

class BSPGraphBasicTests (unittest.TestCase):
    def test_initialize_is_defined(self):
        #First, we will make sure an exception is raised if it isn't defined
        test_graph = BSPGraph(10, BSPNode)
        self.assertRaises(Exception, test_graph.initialize)

        #Now, we will make sure one isn't raised if it is defined
        class TestGraph (BSPGraph):
            def initialize(self):
                pass

        test_graph = TestGraph(10, BSPNode)
        test_graph.initialize()

    def test_add_undirected_edge(self):
        test_graph = BSPGraph(2, BSPNode)
        test_graph.add_undirected_edge(0, 1, 2)

        self.assertEqual(test_graph.nodes[0].edges, [Edge(0, 1, 2)])
        self.assertEqual(test_graph.nodes[1].edges, [Edge(1, 0, 2)])

    def test_send_message(self):
        test_graph = BSPGraph(10, BSPNode)
        test_graph.send_message(Message(1, 1337))
        self.assertEqual(test_graph.master_inbox[0], Message(1, 1337))

    def test_deliver_messages(self):
        test_graph = BSPGraph(10, BSPNode)
        test_graph.send_message(Message(5, 7))
        test_graph.deliver_messages()
        self.assertEqual(test_graph.nodes[5].inbox[0], Message(5, 7))

class BSPGraphRunTests (unittest.TestCase):
    def test_run_end_when_all_nodes_asleep(self):
        class SleepNode (BSPNode):
            def step(self):
                self.deactivate()

        class TestGraph (BSPGraph):
            def initialize(self):
                pass

        test_graph = TestGraph(10, SleepNode)
        test_graph.run()
        #We want to assert that the step run() ended on is two,
        #because all nodes should be asleep after step one.
        self.assertEqual(test_graph.current_step, 2)


if __name__ == '__main__':
    unittest.main()
