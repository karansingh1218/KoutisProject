import networkx as nx

def strongly_connected(Graph):
  results = nx.strongly_connected_components(Graph)
  return results

def weak_connected(Graph):
  results = nx.weakly_connected_components(Graph)
  return results
  


