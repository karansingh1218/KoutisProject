import networkx as nx
import pandas as pd
import numpy as np
import heapq
import math
from indegree import *
from undirectedgraphs import *
from dataparse import *
import resource, sys
from DFSalgo import *
from itertools import groupby
from cycles import *
import os 
from KosarajuUpdated import *
from Recommendation import *
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

"""
1. The Data

1) Using Custom Data Parser that used Python Pandas to read the text file into the environment.
2) NetworkX is being used to manage the list of edges
"""
# Twitter DataSet --> Directed Graph
twitterEdges = dataParser('twitter_combined.txt', ['nodes', 'edges'])
twDG         = nx.DiGraph()
twDG.add_edges_from(twitterEdges)
tEdge = list(twDG.edges)

# Tiny Directed Graph
tinyDG = dataParser('tinyDG.txt', ['nodes', 'edges'])
smallSample= nx.DiGraph()
smallSample.add_edges_from(tinyDG)
smallSample.number_of_nodes()
smallSample.number_of_edges()
E = list(smallSample.edges())

# Facebook Undirected Graph
faceedges = dataParser('facebook_combined.txt', ['nodes', 'edges'])
G = nx.Graph()
G.add_edges_from(faceedges)
G.number_of_nodes()
G.number_of_edges()
fe = list(G.edges)

"""
Task 2: Finding Influencers

"""

# In-Degree for Directed Graphs (Twitter Graph)
print(nth_highest_degree(n = 100, edges = tEdge))

# Degree of Vertex for Undirected Graphs (Facebook)
results = degree_of_vertex(edges = fe )
foo = follower_counts(results)
print(foo)

"""
Task 3: Cleaning-up the network.

"""

adj_list = adjancency_list(tEdge)
results  = DFS_wrapper_updated(tEdge)
finite_state_machine = []
for i in results:
    finite_state_machine.append(len(i))
# print(finite_state_machine)
l0 = results[0]
l1 = results[1]
inside_network = list(set(l0))
outside_network = list(set(l1) - set(l0))
print("Outside of Network")
print(outside_network)
print("Inside Network")
print(inside_network)

"""
Task 4: Strongly Connected Components
1) Created Iterative Version of the Kosaraju Algoritihim

"""

kso = Kosaraju(tEdge)
kso.adjancency_list()
kso.dfsiLoop()
kso.transpose_graph()
print(kso.dfsiRev())

"""
Task 4: Recommendation Engine

1) Using tiny directed graph, due to memory constraints for repl.it
 
"""
Karan = Recommendation(E,3)
Karan.adjacency_matrix()
Karan.matrix_multiplication()
print(Karan.length_k_chains(0,3))

"""
Bonus Material: Detect Cycles in directed Graphs

"""

cycles_in_graph = cycle_DFS_wrapper(tEdge)

nocyc = 0
cyc = 0 
for key in cycles_in_graph:
    if cycles_in_graph[key] =='Cycles Exist at the specified Node':
        cyc = cyc + 1 
    else:
        nocyc = nocyc  + 1

print("Cycles in graph: {} ".format(cyc) )
print("No Cycles in graph: {} ".format(nocyc) )
print("Total Nodes in graph for verification: {}".format(cyc + nocyc))