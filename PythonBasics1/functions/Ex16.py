"""
var arg function: a function that takes any umber of arguments.

sum of any numbers:
"""

def sum(*numbers):
    res = 0
    for n in numbers:
        res = res + n
    return res


print(sum(1,1,13,1,13,24,245,35,43,35,25,36,3,7,36,5,436,45,4,57,457,7))

print(sum(1,1,13,1,13,24))
