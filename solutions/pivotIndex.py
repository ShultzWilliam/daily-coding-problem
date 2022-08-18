#Given an array of integers nums, calculate the pivot index of this array
#
#The pivot index is the index where the sum of all numbers strictly to the left of the index 
# s equal to the sum of all numbers strictly to the index's right.
#
#Return the leftmost pivot index. If no such index exists, return -1

def pivotIndexSlow(nums) -> int:
    for i in range(len(nums)):
        leftSum = sum(nums[:i])
        rightSum = sum(nums[i+1:])
        if leftSum == rightSum:
            return i
    return -1

def pivotIndex(nums) -> int:
    totalSum = sum(nums)
    left = 0
    for i, x in enumerate(nums):
        if left == totalSum - left - x:
            return i
        left += x
    return -1


print(pivotIndex([1,7,3,6,5,6]))

print(pivotIndex([1,2,3]))

print(pivotIndex([2,1,-1]))