#Create a function that performs a binary search on the target array titled "nums"
#The functions takes two inputs: a target array "nums" and the target within the array "target"
#Example: nums = [1,3,6,9,12,17] | target = 9       -> returns 3
#If the target can not be found in the given array, return -1

def binarySearch(nums, target):
    left,right = 0, len(nums)-1

    while left <= right:
        pivot = left + (right-left)//2
        curVal = nums[pivot]

        if target == curVal:
            return pivot
        elif target < curVal:
            right = pivot-1
        else:
            left = pivot +1
    
    return -1



def testBinarySearch():
    nums = [[1],
               [1,3,6,789],
               [12,14,378,4657,99999],
               [-100,-79,-65,-5,0,1,12,123,1456],
               [1,4,17,100]]

    targets = [1,6,99999,12,2]

    for i in range(len(nums)):
        print(binarySearch(nums[i],targets[i]))

testBinarySearch()
