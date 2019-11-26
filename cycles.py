from DFSalgo import adjancency_list

def check_cycles(graph, node):
    """Run DFS through the graph from the starting
    node and return the nodes in order of finishing time and
    check if cycles exists at each specified node. This is considered an exhaustive search
    """
    
    seen = {node}
    stack = [node]
    cycle = []
    result = []
    
    while stack:
        
        x = stack[-1]

        nxt = set(graph.get(x, [])) - seen

        validate = set(graph.get(x))
        
        if graph.get(x) != []:
        
            checkstack =  all(item in stack for item in validate)
            checkseen  =  all(item in  seen for item in validate)

            if checkstack and checkseen is True:
                return "Cycles Exist at the specified Node"

        if nxt:
            stack.extend(list(nxt))
            seen |= nxt   
        
        else:
            result.append(x)
            stack.pop()    
    
    return "no cycle"

def cycle_DFS_wrapper(edges):
    adj_list = adjancency_list(edges)
    done = {}
    
    for key in adj_list:
        
        results = check_cycles(adj_list, key)
        done[key] = results
    return done
