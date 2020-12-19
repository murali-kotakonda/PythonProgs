"""
var arg function: a function that takes any umber of arguments.

sum of any numbers:
"""

#WRITE THE FUNCTION
def sum(*nums):
    res =0
    for n in nums:
        res= res + n
    print(res)
#sum funtion can be called by passing any number of values

#call the function
sum(1,2)
sum(1,2,24,2,5,21,36,25,343,7,25,7,25,43,3256,47)
sum(10,20,30)
sum(1,2,42,1,4,214,14,4)




