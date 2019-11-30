from DFSalgo import adjancency_list


def kosaraju_wrapper(edges):
  
  # adj_list = adjancency_list(edges)
  # # vertices        = len(adj_list)
  # test = []
  
  # for key in adj_list:
      
  #     results = kosaraju(adj_list,key)
  #     test.append([results])

  i_seent_it = set()
  pathDictionary = {}
  adj_list = adjancency_list(edges)
  # vertices        = len(adj_list)
  test = []

  def transpose_graph(graph):
    """Transpose the adjancency list"""
    G = graph
    res ={}
    for k, val in G.items(): 
    # for k in G.keys():
        # for val in G[k]:
      if val not in res.keys():
          res[val] = [k]
      else:
          res[val].append(k)
    return res

  transposedGraph = transpose_graph(adj_list)
  # for key in adj_list:
      
  #     if key in i_seent_it: 
  #         print("Skipping idx {} bc i seent it".format(key))
  #         continue 
      
  #     results = kosaraju(adj_list,key)
      
  #     for idx in results: 
  #         i_seent_it.add(idx)
  
  #     # pathDictionary[key] = tuples(results)
  #     test.append([results])

  results = kosaraju(adj_list, 12,transposedGraph)
  test.append([results])

  return test

def kosaraju(edges, node,transposedGraph):

  def dfsi(graph, node):
      """Run DFS through the graph from the starting
      node and return the nodes in order of finishing time.
      """
      seen = {node}
      stack = [node]
      result = []
      while stack:
          x = stack[-1]
          nxt = set(graph.get(x, [])) - seen
          if nxt:
              stack.extend(list(nxt))
              seen |= nxt
          else:
              result.append(x)
              stack.pop()
      del result[-1]
      return tuple(result)
  

  def dfs_transposed_outerstack(transposedGraph, outerStack):
      
      seened = set() 
      output = []
      scc = {}
      tg = transposedGraph

      for s in outerStack:
          
          if s in tg[s]:
              tg[s].remove(s)
              # A cycle is found because it is pointing to itself.
              output.append([s])
          
          if s in seened:
              print("skip {} bc seen it".format(s))
              continue
          
          results = dfsi(tg, s)            
      
          for v in results:
              seened.add(v)
          
          print(results)
          # output.append([results])
      
  
  adjList = edges
  outerStack = dfsi(adjList, node)
  scc = dfs_transposed_outerstack(transposedGraph, outerStack)

  return scc