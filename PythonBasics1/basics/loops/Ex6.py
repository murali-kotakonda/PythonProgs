"""

take size as input

o/p:
print all even numbers from 1 till the input

"""

size = int(input("enter num : "))

for i in range(1, size+1):
    if(i%2==0):
        print(i)