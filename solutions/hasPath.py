#Given a graph in the form of a dict, write a function that determines if there
#is a path from one given node in a graph to another given node in a graph
#
#inputs: graph: dict
#        src: str
#         dst: str
#output: bool, true if a path exists, false if it doesnt
#Parameter: The graph is acyclic

#Depth first search approach
from operator import truediv


def hasPath(graph, src, dst) -> bool:
    #Time complexity:
    #   n = number of nodes, e = number of edges
    #   worst case scenario, we traverse every edge, so TC = O(e)
    stack = [src]
    checked = [src]
    while len(stack) > 0:
        cur = stack.pop()
        if cur == dst:
            return True
        for i in graph[cur]:
            if(i not in checked):
                stack.append(i)
    return False

def hasPathR(graph, src, dst) -> bool:
    if (src == dst):
        return True
    
    for i in graph[src]:
       if hasPathR(graph, i, dst) == True:
        return True
    
    return False


def testHasPath():
    graph = {
        'f':['g','i'],
        'g':['h'],
        'h':[],
        'i':['k','g'],
        'j':['i'],
        'k':[]
    }

    for i in graph:
        for j in graph:
            print(f"Results for graph:, {i}, {j}\t\tDepth First Iterative: {hasPath(graph,i,j)},\t\tDepth First Recursive: {hasPathR(graph, i, j)}")

    

testHasPath()
