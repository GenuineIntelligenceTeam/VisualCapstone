from node import Node
import numpy as np

class WeightedGraph(object):

    def __init__(self, descriptors):
        self.nodes = []
        for index, descriptor in enumerate(descriptors):
            self.nodes.append(Node(index, descriptor))
        self.construct_adjacency_matrix()

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
    
    def step(self):
        dict = defaultdict(list)
        i = np.round(np.random.rand()*len(self.A-1))
        for j, node in enumerate(nodes):
            dict[node.ID] += self.A[i,j]
        nodes[i].ID = max(dict,key=dict.get)

    def unique_classes(self):
        return len(set(node.ID for node in nodes))

    def whispers_loop(self, num_classes, max_iterations=1000):
        i = 0
        while self.unique_classes() > num_classes:
            self.step()
            i += 1
            if i == max_iterations:
                break

    def __len__(self):
        return len(self.nodes)
