n1 =  int(input("enter num1 "))
n2 =  int(input("enter num2 "))
n3 =  int(input("enter num3 "))


if n1 > n2:
    #big is between n1 and n3
    if n1 > n3:
        print("Big = ", n1)
    else:
        print("Big = ", n3)

else:
    # big is between n2 and n3
    if n2 > n3:
        print("Big = ", n2)
    else:
        print("Big = ", n3)