# take numbers as input and perform sum , if the input is negative then stop the program ad print final sum

sum = 0
num = 0

while (num >= 0):
    sum = sum + num
    num = int(input("enter number"))


print(" sum = ", sum)