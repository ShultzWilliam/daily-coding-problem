# Problem: For a given string of letters, compress the string such that
#          "aaabbccccddddd" becomes "a3b2c4f5"
#
#           - The compression function should output a string such that 
#             a decompress function would revert the string to its original
#             form.
#
#           - The function should return a new string value and NOT modify
#             the original input string

def compress(value: str) -> str :
    returnable = ""
    count = 1
    for i in range(len(value)-1):
        if value[i] == value[i+1]:
            count +=1
            continue
        returnable += value[i]+str(count)
        count = 1

    returnable += value[-1]+str(count)
    return returnable

def testCompress():
    print(compress("aaa"))
    print(compress("aaabbbb"))
    print(compress("aaabbbaaaaa"))
    print(compress("abcdefg"))
    print(compress("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaccccccccccccccccccccamfejasfekaaaaaaa"))

        
testCompress()