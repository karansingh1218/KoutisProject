import networkx as nx
import pandas as pd
import numpy as np

def dataParser(filename, columnlist):
    
    data = pd.read_csv(filename, sep=" ", header=None)
    data.columns = columnlist
    subset = data[columnlist]
    tuples =  [tuple(x) for x in subset.values]
    return tuples

class Recommendation:
    """
    i = Person 1
    j = Person 2
    k = The number of length k-chains you are looking for
    edges = Input for edges list

    """
    A = []
    kRaisedMatrix  = []
    
    def __init__(self, edges, k):
        self.edges =  edges
        self.k     = k
        
    def adjacency_matrix(self):
        data = self.edges
        
        nodes = np.unique(data)  # mapping node name --> index
        noidx = {n: i for i, n in enumerate(nodes)}  # mapping node index --> name

        n = nodes.size  # number of nodes

        numdata = np.vectorize(noidx.get)(data)  # replace node id by node index

        A = np.zeros((n, n))
        for tail, head in numdata:
            A[tail, head] = 1
            #A[head, tail] = 1  # add this line for undirected graph
        
        Recommendation.A = A 

        return Recommendation.A
    
    def matrix_multiplication(self):
        Recommendation.kRaisedMatrix = np.linalg.matrix_power(Recommendation.A, self.k)
        return Recommendation.kRaisedMatrix
    
    def length_k_chains(self, i, j):
        
        p1 = i 
        p2 = j 
        
        return Recommendation.kRaisedMatrix[p1][p2]   

