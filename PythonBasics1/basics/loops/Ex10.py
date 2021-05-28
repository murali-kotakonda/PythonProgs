"""

take number  as input

o/p:
print factorial of the number

i/p: 5

o/p:  120 ( 5* 4* 3* 2 * 1)

"""
size = int(input("enter size : "))

fact = 1

for i in range(1, size+1 ):
    fact = fact * i

print(fact)
