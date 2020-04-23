x, y = input("Enter a two value: ").split() 
print("Number of boys: ", x) 
print("Number of girls: ", y) 
print() 
  
# taking three inputs at a time 
x, y, z = input("Enter a three value: ").split("#") 
print("x: ", x) 
print("y: ", y) 
print("z", z) 
print() 
 
  
# taking two inputs at a time 
a, b = input("Enter a two value: ").split() 
print("First number is {} and second number is {}".format(a, b)) 
print() 
  
# taking multiple inputs at a time  
# and type casting using list() function 
x = list(map(int, input("Enter a multiple value: ").split())) 
print("List of students: ", x) 