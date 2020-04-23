id = int(input("enter user id "))
age = int(input("enter user age"))
type = input("enter user type")
if (id > 0 and age > 18 and type=="admin"):

    print("details are valid")
else:
    print("details are not valid")

