num1 = int(input("Enter num1"))
num2 = int(input("Enter num2"))
num3 = int(input("Enter num3"))

big = num1

if(num2>big):
    big= num2

if(num3>big):
    big= num3

print("big = ", big)