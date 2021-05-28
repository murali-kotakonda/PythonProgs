"""
take input for id , age , usertype
validate id & age , usertype

if id is valid then only validate the age [ when id is invalid dont validate further ]
if age is valid then only validate the usertype[ when age is invalid dont validate further ]

at a time only one condition is executed
solution)
if + elif
"""

id = int(input("enter id :" ))
age = int(input("enter age :"))
userType = input("enter userType :")


if id<0 :
    print("invalid id")
elif age<18:
    print("id is valid")
    print("invalid age")
elif userType!="admin":
    print("id is valid")
    print("age is valid")
    print("invalid userType")
else:
    print("valid id, age , usertype")

