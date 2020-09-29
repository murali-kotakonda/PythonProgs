"""
find big of three numbers
"""
n1 =  int(input("enter num1 "))
n2 =  int(input("enter num2 "))
n3 =  int(input("enter num3 "))

#assign n1 value to big
big = n1

#compare with n2
if(n2>big):
    big= n2

#compare with n3
if(n3>big):
    big = n3

print("Bigger =", big)





