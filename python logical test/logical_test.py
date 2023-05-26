# Python Logical Test
# Write a Python function that prints all consecutive incremental numbers from a string of numbers.
# Example:
# Input: '588432347423122345'
# Output: '234', '23', '12', '2345'





"""Solution 1"""
def cons_increment(s):
    l = int(len(s))
    # cons_list = []
    word = ""
    check = None
    for i in range(l-1):
        if int(s[i])+1 == int(s[i+1]):
            word += s[i]
            check = True
        else:
            if check == True:
                word += s[i]
            check= False
            word += " "

        if (i == l-2) and check == True:
            word += s[i+1]
    print(word.split())
    return word.split()

cons_increment('588432347423122345')



"""Solution 2"""
def cons_incrementv2(s):
    l = int(len(s))
    # cons_list = []
    word = ""
    check = None
    for i in range(l):
        try:
            if int(s[i])+1 == int(s[i+1]):
                word += s[i]
                check = True
            else:
                if check == True:
                    word += s[i]
                check= False
                word += " "
        except IndexError:
            word += s[i]


    print(word.split())
    return word.split()

cons_incrementv2('588432347423122345')