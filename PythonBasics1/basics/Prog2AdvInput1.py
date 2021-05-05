"""
How to take multiple data as input in single line

earlier:
a =input("enter data : ")
b =input("enter data : ")
c= input("enter data : ")

Now:
a,b,c = input("enter data : ").split()

"""

x, y = input("Enter a two value: ").split() 
print("x value: ", x) 
print("y value: ", y) 

  
  
# taking three inputs at a time 
x, y, z = input("Enter a three value: ").split() 
print("x : ", x) 
print("y  : ", y) 
print("z : ", z) 
print() 



x ,y,z =input("enter three values").split("#")
print("x= ",x)
print("y= ",y)
print("z= ",z)

print("First number is ", x, " and second number is " ,y , " 33rd value = ",z)
print("First number is {} and second number is {}, 33rd value = {}".format(x,y,z))
# taking two inputs at a time 
a, b = input("Enter a two value: ").split() 
print("First number is {} and second number is {}".format(a, b)) 
print() 
  
# taking multiple inputs at a time  
# and type casting using list() function 
x = list(map(int, input("Enter a multiple value: ").split())) 
print("List of students: ", x) 