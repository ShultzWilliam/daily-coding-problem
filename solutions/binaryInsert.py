#Given a sorted array of integers, create a method that inserts a new number into the array at the correct index in O(logn) time
#Input values: nums, a list of ints
#              target, a given int
#Output values: none, none function. It modifies an array but doesn't give  return value

def insert(nums, target):
    left, right = 0, len(nums)-1

    while left <= right:
        pivot = left +(right-left)//2
        cur = nums[pivot]

        if target == cur:
            nums.insert(pivot,target)
            return
        elif target < cur:
            right = pivot-1
        else:
            left = pivot + 1
        
    nums.insert(left, target)    
    return 


    return nums

def testInsert():
    nums = [[0,1,2,3],[100,1000,10000,100000,10000000,200000000,3000000000],[-15,-12,-6,-1,7,12,19]]
    targets = [9,124,3]
    for i in range(len(nums)):
        insert(nums[i],targets[i])
        print(nums[i])

testInsert()