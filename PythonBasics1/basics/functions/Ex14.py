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
num1=90
num2=30
num3 =123

#Approach1
v1 = bigger(num1,num2) #find big of num1,num2
big  = bigger(num3,v1) #find the bigger of v1 and num3
print(big)


#Approach2
big = bigger(num1 , bigger(num2,num3))
print(big)


#find big of 4 numbers
print("*************big of 4 nums*****************")
num1=90
num2=30
num3 =123
num4 = 165
big = bigger(num1 , bigger(num2,bigger(num3,num4)))
print(big)




