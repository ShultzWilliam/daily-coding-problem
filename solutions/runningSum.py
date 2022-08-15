#Given an arrat nums, the running some of an array would be an array such that:
#   runningSum[i] = sum(nums[0]...nums[i])
#
#Create a function that takes an array of integers nums and returns a running sum array


def runningSum(nums):
    returnable = []
    curSum = 0
    for i in nums:
        curSum += i
        returnable.append(curSum)
    return returnable

def testRunningSum():
    testCases = [[0],
                 [1,2,3],
                 [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                 [123,10,7,42,1,6,7,123,56,2,7,2,78,8,1,436,47,586,2,123,73,684,56856,34,534765,8,568,56,23,423,457, 56,8,546]]

    for x in testCases:
        print(runningSum(x))

testRunningSum()