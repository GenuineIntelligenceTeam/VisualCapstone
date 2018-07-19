from node import Node

class WeightedGraph(object):

    def __init__(self, descriptors):
        self.nodes = []

    def __len__(self):
        return len(self.nodes)

