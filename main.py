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
# results  = DFS_wrapper(tEdge)
for line in adj_list:
  print(line)
# from inspect import getsourcefile
# from os.path import abspath

# print(abspath(getsourcefile(lambda:0)))

# graph1 = {
#     'A' : ['B','S'],
#     'B' : ['A'],
#     'C' : ['D','E','F','S'],
#     'D' : ['C'],
#     'E' : ['C','H'],
#     'F' : ['C','G'],
#     'G' : ['F','S'],
#     'H' : ['E','G'],
#     'S' : ['A','C','G']
# }

# def dfs(graph, node):
#     visited = [node]
#     stack = [node]
#     while stack:
#         node = stack[-1]
#         if node not in visited:
#             visited.append(node)
#             print(visited)
#         remove_from_stack = True
#         for next in graph[node]:
#             if next not in visited:
#                 stack.append(next)
#                 remove_from_stack = False
#                 break
#         if remove_from_stack:
#             stack.pop()

#     return visited


# def dfsi(graph, node):
#     """Run DFS through the graph from the starting
#     node and return the nodes in order of finishing time.
#     """
#     seen = {node}
#     stack = [node]
#     result = []
#     while stack:
#         x = stack[-1]
#         nxt = set(graph.get(x, [])) - seen
#         if nxt:
#             stack.extend(list(nxt))
#             seen |= nxt
#         else:
#             result.append(x)
#             stack.pop()
#     return result

# check = dfsi(adj_list, 765)

# for line in check:
#   print(line)
