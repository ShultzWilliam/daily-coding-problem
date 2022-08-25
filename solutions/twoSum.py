#Write a function that returns the indexes of two numbers in a list whose sum equals a given target
#
#EX: List = [2,7,11,15] , target = 9
#       -> [0,1]
#
#Inputs: list: list[int], target: int
#Outputs: list[int]
#
#Assumption: there always exists at least on solution

#method by creating a dictionary which holds the value needed to return the answer, and the returning key
#the dictionary is linearly filled up, and when a solution is found
#it returns the index i and the appropriate value from the dict
def twoSum(nums, target):
    dict = {}

    for i in range(len(nums)):
        if nums[i] in dict:
            return [dict[nums[i]],i]
        dict[target-nums[i]] = i

    #if no solution is found, return this instead
    return [-1,-1]

#This brute force alg checks all possible cases to find the appropriate indices
#Unlike the top alg which uses O(N) time, this alg's time complexity would be O(N^2)
def bruteForceTwoSum(num, target):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i] + num[j] == target:
                return [i,j]
    return [-1,-1]



def test():
    ex = [
        [2,7,11,15],
        [3,2,4],
        [3,3],
        [3,3,3,3,3,7,3,3,3,3,3,3,7,3,3,3,3,1,3,3,1]]

    target = [9,6,6,14]

    for i in range(len(ex)):
        print(twoSum(ex[i],target[i]))
    print("")
    for i in range(len(ex)):
        print(bruteForceTwoSum(ex[i],target[i]))
