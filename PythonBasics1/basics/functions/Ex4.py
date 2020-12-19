"""
write a function that takes 2 nums as input and prints the bigger number.

"""


#how to write function
def big(x,y):
     bigger=0
     if(x>y):
         bigger=x
     else:
         bigger = y
     print("Big = ", bigger)

 # x, y , bigger are the local variables

#how to call the function
big(30,13)

n1=56
n2=90
big(n1,n2)

n3= int(input("enter num1"))
n4= int(input("enter num2"))
big(n3,n4)

#n1,n2,n3,n4 are global variables.