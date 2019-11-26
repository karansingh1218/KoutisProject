"""
The Degree Of Vertex for Undirected Graphs
"""
def degree_of_vertex(edges):
    """
    Find the Degree of Vertex for all of the edge.
    Time Complexity: O(n) --> Not a very fast implementation
    """
    
    dictver = {}
    count = 0
    
    freq = {}
    i = 0
    j = 0
    for i, j in edges:
        
        if ( i in freq):
            
            freq[i] += 1
        else:
            freq[i] = 1
    
    return freq

def follower_counts(results):
    follcounts = []
    for i in results:
        follcounts.append(results[i])
    return follcounts
