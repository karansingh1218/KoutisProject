import networkx as nx
import pandas as pd
import numpy as np
import heapq
import math
from indegree import *
# from undirectedgraphs import *
from dataparse import *
# from TarganAlgorithim import *
import resource, sys
from DFSalgo import *
from itertools import groupby
from cycles import *
import os 
# dirName = "tempDir"
# if not os.path.exists(dirName):
#     os.mkdir(dirName)
#     print("Directory " , dirName ,  " Created ")
# else:    
#     print("Directory " , dirName ,  " already exists")

# print(os.path.exists("tempDir/1084.txt"))
# f= open('tempDir/1084.txt')
# first_char= f.read(1)
# print(first_char)
# f.close()

resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)
twitterEdges = dataParser('twitter_combined.txt', ['nodes', 'edges'])
twDG         = nx.DiGraph()
twDG.add_edges_from(twitterEdges)
tEdge = list(twDG.edges)
# twitternthhighest = nth_highest_degree(100,tEdge)
# strongly_connected_components(Graph(tEdge))
# scc     = list(strongly_connected(twDG))
# wcc     = list(weak_connected(twDG))

adj_list = adjancency_list(tEdge)
results  = DFS_wrapper_updated(tEdge)

finite_state_machine = []

for i in results:
    finite_state_machine.append(len(i))

print(finite_state_machine)
l0 = results[0]
l1 = results[1]

inside_network = list(set(l0))
outside_network = list(set(l1) - set(l0))
print(outside_network)


cycles_in_graph = cycle_DFS_wrapper(tEdge)

nocyc = 0
cyc = 0 
for key in cycles_in_graph:
    if cycles_in_graph[key] =='Cycles Exist at the specified Node':
        cyc = cyc + 1 
    else:
        nocyc = nocyc  + 1
print(cyc, nocyc)
print(cyc + nocyc)

 