#Given an array of numbers nums[], return an array of numbers send[] where
#send[i] is equal to the quantity of number that are smaller than the number nums[i]
#
# example: [1,4,67,8,9] -> [0,1,4,2,3]
#          [7,7,7] -> [0,0,0]
#

def slowSmallerThan(nums):
    send = []
        
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[j] < nums[i]:
                count += 1
        send.append(count)
    return send

def fastSmallerThan(nums):
    sorted_nums = sorted(nums)
    return [sorted_nums.index(i) for i in nums]



def test():
    tests = [
        [1,2,3,4,5],
        [1,2,3,4,5,4,3,2,1],
        [1],
        [100,1000,10000001,100000000000,1,0]
        ]
    
    answers = [
        [0,1,2,3,4],
        [0,2,4,6,8,6,4,2,0],
        [0],
        [2,3,4,5,1,0]
    ]

    print("Testing slow Smaller Than method:")
    for i in range(len(tests)):
        print(f"Test {i+1}: {answers[i] == slowSmallerThan(tests[i])}")

    print("Testing fast Smaller Than method:")
    for i in range(len(tests)):
        print(f"Test {i+1}: {answers[i] == fastSmallerThan(tests[i])}")
