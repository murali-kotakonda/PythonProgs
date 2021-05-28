"""
var arg function: a function that takes any umber of arguments.

sum of any numbers:
"""

def big(*numbers):
    res = numbers[0]
    for num in numbers:
        if num > res:
            res = num

    return res


print(big(1,1,13,1,13,24,245,35,43,35,25,36,3,7,36,5,436,45,4,57,457,7))

print(big(1,1,13,1,13,24))

print(big(1,1,13,1,13,24,3,35,2,25,25,53,325,35,25,36,325,63,532))
