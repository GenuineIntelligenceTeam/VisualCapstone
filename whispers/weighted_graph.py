from node import Node
import numpy as np
from collections import defaultdict

"""
Class implementing a weighted graph for whispers clustering.
Stores an adjacency matrix representing distances as well as a list of image file nodes.
"""
class WeightedGraph(object):

    """
    Initialize a weighted graph from descriptors.

    Parameters:
        descriptors: List[Tuple[Tuple]]
            List of descriptor vectors and their associated filepaths
    """
    def __init__(self, descriptors):
        self.nodes = []
        for index, (fpath, descriptor) in enumerate(descriptors):
            self.nodes.append(Node(index, descriptor, fpath))
        self.construct_adjacency_matrix()

    """
    Constructs a new adjacency matrix for all descriptors. Called during initialization to prepare for
    whispers algorithm steps.
    """
    def construct_adjacency_matrix(self):
        self.A = np.empty(( len(self), len(self) ))

        # Iterate over node list twice to initialize full A-matrix
        for i, node_i in enumerate(self.nodes):
            for j, node_j in enumerate(self.nodes):
                if np.isclose(node_i.distance(node_j), 0):
                    self.A[i, j] = 0
                else:
                    self.A[i, j] = node_i.distance(node_j)

        # Generate a histogram of all distances
        histogram, bin_edges = np.histogram(self.A.flatten(), bins=len(self), density=True)

        # Obtain threshold from cumulative sum
        cumulative_distr = np.cumsum(histogram * np.diff(bin_edges))
        threshold = bin_edges[np.searchsorted(cumulative_distr, 0.1)]

        # Apply threshold to adjacency matrix and map d --> 1/d^2
        for index in np.ndindex(self.A.shape):
            if self.A[index] > threshold:
                self.A[index] = 1.0 / (self.A[index] ** 2)
            else:
                self.A[index] = 0

    """
    Step through the whispers algorithm once, updating a random node based on highest
    sum-weighted neighbors.
    """
    def step(self):
        dict = defaultdict(int)
        i = int(np.round(np.random.rand()*len(self.A)-1))
        for j, node in enumerate(self.nodes):
            dict[node.ID] += self.A[i,j]
        self.nodes[i].ID = max(dict,key=dict.get)

    """
    Helper function returning total number of classes.
    """
    def unique_classes(self):
        return len(set(node.ID for node in self.nodes))

    """
    Loop through the whispers algorithm for a given number of iterations, or until the number of
    classes has converged to a desired value.

    Parameters:
        num_classes: int
            Number of desired classes in the data.

        max_iterations: int
            Maximum number of iterations to perform in cases of non-convergence.
    """
    def whispers_loop(self, num_classes, max_iterations=1000):
        i = 0
        while self.unique_classes() > num_classes:
            print(self.unique_classes())
            self.step()
            i += 1
            if i == max_iterations:
                break

    def __len__(self):
        return len(self.nodes)
