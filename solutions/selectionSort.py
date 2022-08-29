#Given an unsorted list, implement the Selection sort algorithm to sort the list in ascending order
#INPUT: in: list[int]
#OUTPUT: list[int]

def swap(a,b):
    temp = a
    a = b
    b = temp

def sort(x):
    returnable = []
    for i in range(len(x)):
        lowest = x[i]
        for j in range(i,len(x)):
            if x[j] <= lowest:
                lowest = x[j]
        returnable.append(lowest)
    return returnable

def test():
    a = [4,7,1,6,9,5,2,6]
    sort(a)


    print(sort(a))
