# Python program showing 
# how to take multiple input 
# using List comprehension 
  
# taking two input at a time 
x, y = [int(x) for x in input("Enter two value: ").split()] 
print("First Number is: ", x) 
print("Second Number is: ", y) 
print() 


# taking three input at a time 
x, y, z = [int(x) for x in input("Enter three value: ").split()] 
print("First Number is: ", x) 
print("Second Number is: ", y) 
print("Third Number is: ", z) 
print() 
  
# taking two inputs at a time 
x, y = [int(x) for x in input("Enter two value: ").split()] 
print("First number is {} and second number is {}".format(x, y))
print("First number is {0} and second number is {1}".format(x, y))
print(f"First number is {x} and second number is {y}")
print("First number is %d and second number is %d"%(x, y)) # %s, %f, %.2f , %.3f

print() 
  
# taking multiple inputs at a time  
x = [int(z) for z in input("Enter multiple value: ").split()] 
print("Number of list is: ", x)  