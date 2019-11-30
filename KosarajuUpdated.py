class Kosaraju():
    
    graph      = {}
    seen       = {}
    transGraph = {}
    Stack      = []
    i_seent_it  = set() 
    newSeen     = set()
    int_seen    = set()
    results     = []
    
    def __init__(self, edges):
        self.edges = edges 
                
    def adjancency_list(self):
    
        adjList = {}

        for node in sorted(self.edges):
            if node[0] not in adjList:
                adjList[node[0]] = [node[1]]
            else:
                adjList[node[0]].append(node[1])

        for node in sorted(self.edges):
            if node[1] not in adjList:
                adjList[node[1]] = []
        
        Kosaraju.graph = adjList

        return Kosaraju.graph

    def transpose_graph(self):
        G = self.graph
        res = {}
        for k in G.keys():
            for val in G[k]:
                if val not in res.keys():
                    res[val] = [k]
                else:
                    res[val].append(k)
        
        Kosaraju.transGraph = res
        
        return Kosaraju.transGraph
    
    
    def dfsi(self, node):
        """Run DFS through the graph from the starting
        node and return the nodes in order of finishing time.
        """        
        graph  = self.graph
        self.seen   = {node}
#         self.seen = self.i_seent_it
        stack  = [node]
        result = []
        
        while stack:
            x = stack[-1]
            nxt = set(graph.get(x, [])) - self.seen
            if nxt:
                stack.extend(list(nxt))
                self.seen |= nxt
            else:
                result.append(x)
                stack.pop()
                
        self.Stack = result
        
        return self.Stack
    
    
    def dfsiLoop(self):
        
        """ Run through each vertex and if already seened it will skip it"""
        
        test  = []
        
        for key in self.graph:
            if key in self.i_seent_it:
                print("skiping id: {}".format(key))
                continue
            
            results = self.dfsi(key)
            print(results)
            
            for idx in results:
                self.i_seent_it.add(idx)
        
        
            test.append(results)
            
        self.Stack = test[-1]
        
        return test[-1]
        
    def dfsiRev(self):
        """Run DFS through the graph from the starting
        node and return the nodes in order of finishing time.
        """        
        transGraph  = self.transGraph
        result = []
        tempStack = []
        results = []
    
        for node in self.Stack:

            if node in self.newSeen:
                print("Skip {}".format(node))
                continue
            
            run = self.dfsik(node)
                
            for v in run:
                self.newSeen.add(v)
                
            print(run)
            
            results.append(run)
            
        return results
    
    def dfsik(self, node):
        """Run DFS through the graph from the starting
        node and return the nodes in order of finishing time.
        """        
        stack  = [node]
        result = []

        while stack:
            
            x = stack[-1]
            
            nxt = set(self.transGraph.get(x, [])) - self.int_seen
            
            if nxt:
                
                stack.extend(list(nxt))
                self.int_seen |= nxt
                
            else:
                result.append(x)
                stack.pop()
                
        self.results = result
        
        return self.results
