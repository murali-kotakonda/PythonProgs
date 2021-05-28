"""

take size as input

o/p:
print sum of all numbers from 1 till the input

i/p: 5

o/p: 15
"""

size = int(input("enter size : "))
sum =  0

#logic
for i in range(1,size+1 , 1):
    sum = sum + i

print("sum = ", sum)
