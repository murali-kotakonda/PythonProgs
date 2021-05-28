"""
take size as input.

take the numbers as input for size no of time

assignment:
Find the bigger number
Find the smaller number
Find the sum

how many numbers:
i/p: 3

what are the numbers:
10
20
30

sum : 60
bigg : 30
small : 10

"""


size = int(input("how many numbers: "))
big  =0
small =0

sum =0

for i in range(size):

    num = int(input("enter number : "))
    if (i == 0):
        big = small = num

    if(num>big):
        big = num

    if(num < small ):
        small = num

    sum = sum + num


print("sum = ",sum)
print("big = ",big)
print("small =",small)

