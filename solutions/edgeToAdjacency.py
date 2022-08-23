#Write a program that takes a graph represented through edges in the form of a list to a an adjacency matrix in the form of a dict
#
#Input: a list of lists of 2 things (very specific)
#
#Output: an adjacency list for a graph in the form of a dict
#
#note: This a is a sort of helper function used for transforming one graph representation into another representation, not a fully fledged alg

#INPUT = [
#    ['i','j'],
#    ['k','i'],
#    ['m','k'],
#    ['k','l'],
#    ['o','n']
#]


def edgeToAdjacency(edges) -> dict:
    output = dict()
    for i in input:
        a,b = i[0], i[1]
        if a not in output:
            output[a] = []
        if b not in output:
            output[b] = []
        output[a] += b
        output[b] += a
    return output

#print(edgeToAdjacency(INPUT))



