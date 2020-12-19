"""

function that takes two nums as input and find the big of two nums
"""

#WRITE THE FUNCTION
def bigger(n1,n2):
    if(n1>n2):
        return n1
    else:
        return  n2



#call the function
num1=10
num2=30

v1 = bigger(num1,num2)
print("bigger of {} and {} is {}".format(num1,num2,v1))

num1=80
num2=20

v2 = bigger(num1,num2)
print("bigger of {} and {} is {}".format(num1,num2,v2))




