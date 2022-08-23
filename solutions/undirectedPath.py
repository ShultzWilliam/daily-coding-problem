#Given an undirected graph "edges", create a function that states
#whether or not two points on the given graph have a path between them
#return true if there is a path, and false if there is no path
#
#INPUTS: input, a list of lists with two strings, representing connections between nodes
#        src,   the starting point node
#        target, the ending node
#OUTPUTS: bool value, true if path exists, false if it doesn't exist

input = [
    ['i','j'],
    ['k','i'],
    ['m','k'],
    ['k','l'],
    ['o','n']
]

#undirectedPath(edges, j, m) //returns true

def buildGraph(edges):
    graph = {}
    
    for i in edges:
        a,b = i[0], i[1]
        if (not (a in graph)):
            graph[a] = []
        if (not (b in graph)):
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph

def undirectedPath(edges, src, target):
    #convert the input into an adjacency matrix
    #perform a BFT or DFT to traverse through the graph
    #***record travelled nodes so as to avoid infinite cycling
    if src == target:
        return True
    #build graph from edges
    graph = buildGraph(edges)

    #perform DFT
    stack = [src]
    visited = set()

    while len(stack) > 0:
        cur = stack.pop()
        print(cur)
        visited.add(cur)
        if cur == target:
            return True
        for i in graph[cur]:
            if i not in visited:
                stack.append(i)
    
    return False


def testUndirectedPath():
    print(f"Printing undirectedPath results for - j, m - {undirectedPath(input,'j','m')}")
    print(f"Printing undirectedPath results for - o, n - {undirectedPath(input,'o','n')}")
    print(f"Printing undirectedPath results for - j, o - {undirectedPath(input,'j','o')}")
    print(f"Printing undirectedPath results for - j, j - {undirectedPath(input,'j','j')}")