#   There are 3 components in the given graph shown below, and the largest components has a size of 4
#   |-------------------|
#   |  O-O-O        O   |
#   |    |   O-O    |   |
#   |    O        O-O   |
#   |-------------------|
#
#   Write a function that finds the size of the largest component in a given graph
#
#   INPUTS: graph
#   OUTPUT: int

def largestComponent(graph) -> int:
    maxCount = 0
    visited = set()

    #Iterate through the graph
    for i in graph:
        #If i is not in visited, we found a new component of the graph - begin traversal
        if i not in visited:
            #DFT for the traversal
            count = 0
            stack = [i]

            while len(stack) > 0:
                cur = stack.pop()
                #print(cur)
                count += 1
                visited.add(cur)
                for j in graph[cur]:
                    if j not in visited:
                        stack.append(j)
                        visited.add(j)
            
            if count > maxCount:
                maxCount = count
            #print("")

    return maxCount

def testLargestComponent():
    test1 = {
    1: [],
    2: [3],
    3: [2],
    4: [5,6],
    5: [4,6],
    6: [4,5],
    7: [8,10],
    8: [7,9],
    9: [8,10],
    10: [7,9]
    }

    test2 = {
    1: [],
    2: [3],
    3: [2]
    }

    test3 = {
    1: [],
    2: [3],
    3: [2],
    4: [5,6],
    5: [4,6],
    6: [4,5]
    }


    test4 = {
        1: [2,3,4,5,6,7,8,9],
        2: [1,3,4,5,6,7,8,9],
        3: [1,2,4,5,6,7,8,9],
        4: [1,2,3,5,6,7,8,9],
        5: [1,2,3,4,6,7,8,9],
        6: [1,2,3,4,5,7,8,9],
        7: [1,2,3,4,5,6,8,9],
        8: [1,2,3,4,5,6,7,9],
        9: [1,2,3,4,5,6,7,8],
        10: [12,11],
        11: [10,12],
        12: [10,11],
        13: [14],
        14: [13,15],
        15: [14,16],
        16: [15,17],
        17: [16,18],
        18: [19],
        19: [20],
        20: [19,21],
        21: [18, 22],
        22: [23, 24],
        23: [],
        24: []
    }

    test5 = {}
    print(f"TEST CASE\tRESULT\t\tEXPECTED\tPASS/FAIL(True/False")
    print(f"Case 1\t\t{largestComponent(test1)}\t\t4\t\t{largestComponent(test1) == 4}")
    print(f"Case 2\t\t{largestComponent(test2)}\t\t2\t\t{largestComponent(test2) == 2}")
    print(f"Case 3\t\t{largestComponent(test3)}\t\t3\t\t{largestComponent(test3) == 3}")
    print(f"Case 4\t\t{largestComponent(test4)}\t\t12\t\t{largestComponent(test4) == 12}")
    print(f"Case 5\t\t{largestComponent(test5)}\t\t0\t\t{largestComponent(test5) == 0}")