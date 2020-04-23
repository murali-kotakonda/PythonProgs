# take numbers as input and perform sum , if the input is negative then stop the program

sum = 0
num = 0

while num >= 0:
    num = int(input("enter number"))
    if (num > 0):
        sum = sum + num

print(" sum = ", sum)