"""

take number  as input

o/p:
print factorial of the number

"""
size = int(input("enter number : "))

fact = 1

for i in range(1,size+1):
     fact = fact * i


print("factorial = " ,fact)


