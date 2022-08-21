#Write a function that goes through a list and searches for a value in a linear fashion
#The function should return the index where the target value is found
#Return -1  if the function can not find the target
#
#Input Values: nums - list<int>
#              target - int
#Output Value: Index of target - int
#
#Note: This search returns the index of the FIRST instance of a value equal to the target value
#Parameter: the list contains no duplicate values

def search(nums, target):
    for i in range(len(nums)):
        if target == nums[i]:
            return i
    return -1

def testSearch():
    nums = [[1,2,3],[123,234,357,468,568,457,346,235,1235,325,6234,457,68],[123123,124,134,5,235,346,457,5686,345234234,436,4575,634,523,423,34,54,2,67,78,834,3],[]]
    targets = [2,68,2,2]
    for i in range(len(nums)):
        print(search(nums[i],targets[i]))
    return

testSearch()