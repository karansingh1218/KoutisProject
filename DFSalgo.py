import os
fileDir = os.path.dirname(os.path.realpath('__file__'))

filepath = ".//" + "dataset//"

def adjancency_list(edges):
    
    adjList = {}

    for node in sorted(edges):
        if node[0] not in adjList:
            adjList[node[0]] = [node[1]]
        else:
            adjList[node[0]].append(node[1])

    for node in sorted(edges):
        if node[1] not in adjList:
            adjList[node[1]] = []

    return adjList


def DFS(adjanceylist, start, vertices):
    
    visited = [False for i in range(vertices)]
    
    stack = [] 
    
    stack.append(start)
    
    path = []
    
    while(len(stack)): # While it is not empty 
        start = stack[-1]
        stack.pop()
        
        if (not visited[start]):  
            
                print(start, end=' ') 
                path.append(start)
                
                visited[start] = True 
                
        # Get all adjacent vertices of the popped vertex s  
        # If a adjacent has not been visited, then push it  
        # to the stack.
        try:
            for node in adjanceylist[start]:  
                if (not visited[node]):  
                    stack.append(node)
        except Exception as e:
            continue
    return path


def DFS_wrapper(edges):
    

    pathDictionary = {}
    adj_list = adjancency_list(edges)
    # vertices        = len(adj_list)
    test = []
    
    for key in adj_list:
        # F = open('tempDir/{}.txt'.format(key), 'w')
        F = open('conneceted_components.txt', 'a+')
        results = dfsi(adj_list,key)
        
        # pathDictionary[key] = tuples(results)
        # test.append(results)
        # F.write(str(results))
        F.write(str(results) + "\r\n")
        F.close()
    # return test

def iterative_dfs(graph, start, path=[]):
    q=[start]
    while len(q):
        v=q.pop(0)
        if v not in path:
          path=path+[v]
          q=graph[v]+ q
    
    print(path)

    return path

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
    return tuple(result)