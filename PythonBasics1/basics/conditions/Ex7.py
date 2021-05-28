"""
take input for id , age , usertype
validate id & age , usertype

if id is valid then only validate the age [ when id is invalid dont validate further ]
if age is valid then only validate the usertype[ when age is invalid dont validate further ]
"""

id = int(input("enter id :" ))
age = int(input("enter age :"))
userType = input("enter userType :")

if id >0 :
    print("valid id")

    if age > 18:
        print("valid age")

        if userType == "admin":
            print("valid usertype")
        else:
            print("invalid userType")
    else:
        print("invalid age")
else:
    print("invalid id")



