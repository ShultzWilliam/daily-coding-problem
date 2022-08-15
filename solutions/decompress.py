#   Problem 2: For a given string of characters and numbers such as "a5b2c3d4",
#              write a function decompress() such that it returns a string which
#              prints "aaaaabbcccdddd"
#              
#              - The function should return a string value and not modify the
#                the original input string

def decompress(value: str):

    #declare variables used: the returnable string, a pairs value, and a temp holder 'prev'
    returnable = ""
    pairs = list()
    prev = value[0]

    #iterate through the input string "value"
    for i in range(1, len(value)):
        #if the cur pointer is a digit, append it to prev
        if value[i].isdigit():
            prev += value[i]
        #if it's not a digit, its a new symbol. Append the prev into the list ex: 'a7', 'b24'
        else:
            pairs.append(prev)
            prev = value[i]

    #lastly, append the last prev into the list
    pairs.append(prev)

    #pairs should be something like ['<symbol><freq>','<symbol><freq>',...]
    #for each pair
    for i in pairs:
        #var for the symbol
        cur = i[0]
        #var for the number of times the symbol occurs
        freq = int(i[1:len(i)])
        for j in range(freq):
            #append the symbol an equal amount of times according to its frequency
            returnable += cur
        
    #return the given string
    return returnable

def testDecompress():
    #should print "aaaaabbcccdddd"
    print(decompress("a5b2c3d4"))

    #new issue: sometimes numbers will be more than 1 symbol, account for frequencies greater than 9, 99, etc.
    print(decompress("f3m7a10b24"))

    print(decompress("a1"))
