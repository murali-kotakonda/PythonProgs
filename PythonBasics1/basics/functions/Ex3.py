"""
write a function that performs sum of two nums.

"""

#how to write function
def sum(x, y):
    r = x+y
    print("sum = " , r)
#here x,y,r are local variables

#how to call the function
sum(10,20)

n1=56
n2=90
sum(n1,n2)

n3= int(input("enter num1"))
n4= int(input("enter num2"))
sum(n3,n4)

"""
 local variable:
     variable created inside the function
     
global variable:
      variable created outside the function or in global area  

here x,y,r are local variables
n1,n2,n3,n4 are global variables.
sum() is a global function.


"""