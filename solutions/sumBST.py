#Given a Binary Search tree, create a function for the search tree that
#returns the sum of the nodes between a given low and high node value
#
#INPUTS: root: treeNode
#        low: int
#        high: int
#
#OUTPUT: int
#
#
#
#EX:
# tree -> [10,5,15,3,7,null,18]
# low  -> 7
# high -> 15
# should return 7 + 10 + 15 = 32

class treeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

a = treeNode(10)
b = treeNode(5)
c = treeNode(3)
d = treeNode(7)
e = treeNode(15)
f = treeNode(18)

a.left = b
b.left = c
b.right = d
a.right = e
e.right = f

def rangeSumBST(root, low: int, high: int) -> int:
        #perform a Depth First Traversal of the BST, charting the values of the given nodes
        record = []
        returning = 0
        stack = [root]
        while len(stack) > 0:
            a = stack.pop()
            record.append(a.val)
            if a.left != None:
                stack.append(a.left)
            if a.right != None:
                stack.append(a.right)
        
        #organize the list so it's in ascending order
        record.sort()
        #take the sum of the nodes within the low-high range
        for i in range(record.index(low),record.index(high)+1):
            returning += record[i]
        return returning

def test():
    result = (rangeSumBST(a,7,15) == 32)
    print(f"result of sumBST on given tree, should return 32: {rangeSumBST(a,7,15)} - result - {result}")

test()

