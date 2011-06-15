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


if __name__ == '__main__':
    unittest.main()
