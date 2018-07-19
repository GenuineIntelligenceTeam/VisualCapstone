import numpy as np

"""
Node in a weighted graph representing the distances in a NxN array
"""
class Node(object):


    """
    Parameters:
        ID: int[0,N]
            ID value for the node in the graph.

        neighbor_weights: List[int]
            List of length N representing weight of edges connecting to each other node in the graph.

        
    """
    def __init__(self, ID, descriptor):
        self.ID = ID
        self.descriptor = descriptor

    def distance(self, other):
        return np.sqrt(np.sum((self.descriptor - other.descriptor) ** 2))