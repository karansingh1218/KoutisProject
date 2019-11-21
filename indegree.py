def write_tuples_to_file(filename, tuplelist):

    with open(str(filename), 'w') as fp:
        fp.write('\n'.join('%s %s' % x for x in tuplelist))

def in_degree(edges):
    
    inDegreeDict = {}
    
    for i, j  in edges:
        
        if j in inDegreeDict:
            inDegreeDict[j] += 1
        
        else:
            inDegreeDict[j] = 1

    return list(inDegreeDict.items())

def mergeSort(array):

    # Base Case
    if len(array) == 1:
        return array

    else:
        # Initialize the iterators
        i = 0
        j = 0

        # Split the array if half, so we can do merge sort
        x = array[:len(array) // 2]
        y = array[len(array) // 2:]

        # activatte the recursive functions of both split arrays
        x = mergeSort(x)
        y = mergeSort(y)

        final = []
        # While loop is needed so the location of i and j do no collide.
        while i < len(x) and j < len(y):
            # Sorts of in ascending order
            if x[i][1] < y[j][1]:
                final.append(x[i])
                i = i + 1
            else:
                final.append(y[j])
                j = j + 1

        final = final + x[i:]

        final = final + y[j:]

    return final

def recursion_reverse(sortedInDegree):
    if len(sortedInDegree) == 0:
        return []  # base case
    else:
        return [sortedInDegree.pop()] + recursion_reverse(sortedInDegree)  # recusrive case

def looper(n, reversedTuple):
    results = []
    for i in range(0,n):
        results.append(reversedTuple[i])
    return results

def nth_highest_degree(n, edges):
    
    # Obtains the in degree of all of the edges in the directed graph
    unSortedInDegree = in_degree(edges)
    
    # Use Merge-Sort Algorithim to sort all of the edges by ascending order
    sortedInDegree = mergeSort(unSortedInDegree)

    # Since pair of tuples of sorted, you can simply reverse the list of tuples
    reversedTuple = list(reversed(sortedInDegree))
#     reversedTuple = recursion_reverse(sortedInDegree)
    
    # Return list of tuples, according till n-highest points
    nth_highest = looper(n, reversedTuple)
    
    return nth_highest

    