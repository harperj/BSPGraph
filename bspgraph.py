import loader
from bspnode import *

class BSPGraph (object):
    def __init__(self, num_nodes, node_class):
        self.num_nodes = num_nodes
        self.nodes = [node_class(self, node_id) for node_id in xrange(num_nodes)]
        self.master_inbox = []
        self.current_step = 0

    def initialize(self):
        raise Exception("No initialize function defined.  Subclass BSPGraph to implement initialize.")

    def run(self, num_steps = -1):
        all_asleep = False

        while not all_asleep:
            if self.current_step == num_steps:
                print "Reached step limit: " + str(self.current_step) + " steps."
                break

            self.current_step = self.current_step + 1
            all_asleep = True
            self.deliver_messages()
            for node in self.nodes:
                if node.active:
                    all_asleep = False
                    node.step()
        if all_asleep:
            print "All nodes asleep, ending run."


    def add_undirected_edge(self, start, end, weight=1):
        self.nodes[start].add_edge(end, weight)
        self.nodes[end].add_edge(start, weight)

    def build_graph_from_edge_list(self, edge_list):
        for edge in edge_list:
            self.add_undirected_edge(edge[0], edge[1])
        self.remove_duplicate_edges()

    def remove_duplicate_edges(self):
        for node in self.nodes:
            node.remove_duplicate_edges()

    def send_message(self, message):
         self.master_inbox.append(message)

    def deliver_messages(self):
        for message in self.master_inbox:
            if self.nodes[message.to_id].active == False:
                #If a node is inactive and receives a message, it should be reactivated.
                self.nodes[message.to_id].active = True

            self.nodes[message.to_id].inbox.append(message)
        self.master_inbox = []
