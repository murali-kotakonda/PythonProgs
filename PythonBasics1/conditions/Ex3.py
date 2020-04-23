id=int(input("enter id value"))
age=int(input("enter age"))
usertype=input("entyer user type")

if id>=0:

    if age>18:

        if usertype=="Admin":
          print("valid data")
        else:
          print("invalid  usertype")
    else:
          print("invalid age")
else:
    print("invalid id")





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
