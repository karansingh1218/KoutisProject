import pandas as pd

def dataParser(filename, columnlist):
    
    data = pd.read_csv(filename, sep=" ", header=None)
    data.columns = columnlist
    subset = data[columnlist]
    tuples =  [tuple(x) for x in subset.values]
    return tuples