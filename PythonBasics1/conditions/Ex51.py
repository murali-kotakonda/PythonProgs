num1 = int(input("Enter num1"))
num2 = int(input("Enter num2"))
num3 = int(input("Enter num3"))

if (num1 > num2):
    #big is between num1 and num3
    if (num1 > num3):
        print("Big = ", num1)
    else:
        print("Big = ", num3)
else:
    # big is between num2 and num3
    if (num2 > num3):
        print("Big = ", num2)
    else:
        print("Big = ", num3)
