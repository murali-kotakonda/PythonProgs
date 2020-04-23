id=int(input("enter user id "))
age=int(input("enter user age"))
type=input("enter user type")
if (id>0):
    print("id is valid")
else:
        print("id is not valid")
if(age>18):
    print("age is valid")
else:
    print("age is not valid")
if(type=="admin"):
    print("type is valid")
else:
     print("type is not valid")
