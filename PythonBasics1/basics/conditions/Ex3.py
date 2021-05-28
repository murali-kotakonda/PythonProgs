"""
//take input for id , age ,usertype

//validate id & age , usertype

//if id is positive print valid id , if not print invalid id

//if age is greater than 18 print valid age else print invalid age

//if usertype is "admin" print valid usertype else print invalid usertype

"""

id = int(input("enter id :" ))
age = int(input("enter age :"))
usetType = input("enter userType :")


if id >0 :
    print("valid id")
else:
    print("invalid id")

if age> 18:
    print("valid age")
else:
    print("invalid age")

if usetType == "admin":
    print("valid usertype")
else:
    print("invalid usertype")
