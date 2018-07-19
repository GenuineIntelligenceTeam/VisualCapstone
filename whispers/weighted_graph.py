from node import Node
import numpy as np

class WeightedGraph(object):

    def construct_adjacency_matrix(self):
        self.A = np.empty(( len(self), len(self) ))
        for i, node_i in enumerate(self.nodes):
            for j, node_j in enumerate(self.nodes):
                if np.isclose(node_i.distance(node_j), 0):
                    self.A[i, j] = 0
                else:
                    self.A[i, j] = node_i.distance(node_j)

        histogram, bin_edges = np.histogram(self.A.flatten(), bins=len(self), density=True)
        cumulative_distr = np.cumsum(histogram * np.diff(bin_edges))

        threshold = np.searchsorted(cumulative_distr, 0.5)

        for index in np.ndindex(self.A.shape):
            if self.A[index] < threshold:
                self.A[i, j] = 1.0 / (self.A[i, j] ** 2)
            else:
                self.A[i, j] = 0

        print(self.A)

    def __init__(self, descriptors):
        self.nodes = []
        for index, descriptor in enumerate(descriptors):
            self.nodes.append(Node(index, descriptor))
        self.construct_adjacency_matrix()

    def __len__(self):
        return len(self.nodes)

test = WeightedGraph([np.array([1,2,3]),np.array([1,3,3]),np.array([1,2,3])])