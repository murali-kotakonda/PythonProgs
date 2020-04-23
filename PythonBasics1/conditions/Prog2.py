id = int(input("enter user id "))
age = int(input("enter user age"))
type = input("enter user type")

if (id > 0):
    print("user id is valid")
    if (age > 18):
        print("user age is valid ")
        if (type == "admin"):
            print("usertype is valid")
        else:
            print("usertype is invalid")
    else:
         print("age is  not invalid")
else:
    print("user id is invalid")





id=int(input("enter id value"))
age=int(input("enter age"))
usertype=input("entyer user type")

if id<0:
    print("invalid id")
elif age<18:
    print("invalid age")
elif usertype != "Admin":
    print("invalid  usertype")
else:
    print("valid data")
