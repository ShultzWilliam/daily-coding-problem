#   The number of components in a graph is equal to the number of clustered
#   nodes and edges that only interact with one another 
#   EX: The graph below has three components
#   |-------------------|
#   |  O-O-O        O   |
#   |    |   O-O    |   |
#   |    O        O-O   |
#   |-------------------|
#
#   Write a function that finds the number of components in a given graph
#
#   INPUTS: graph
#   OUTPUT: int

from re import I


input = {
    0: [8,1,5,11],
    1: [0],
    2: [3,4],
    3: [2,4],
    4: [3,2],
    5: [0,8],
    8: [0,5],
    9: [10],
    10: [9],
    11: [0],
    12: []
}

def components(graph) -> int:
    count = 0
    visited = set()

    for i in graph:
        if i not in visited:
            stack = [i]

            while len(stack) > 0:
                cur = stack.pop()
                visited.add(cur)
                for j in graph[cur]:
                    if j not in visited:
                        stack.append(j)
            
            count += 1

    return count

print(f"count of components for input: {components(input)}")