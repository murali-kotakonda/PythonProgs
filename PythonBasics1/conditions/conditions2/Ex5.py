"""
Req:
take input for id , age , usertype

validate id & age , usertype
-> if id is positive print valid id , if not print invalid id
->if age is greater than 18 print valid age else print invalid age
->if usertype is "admin" print valid usertype else print invalid usertype

"""
#take input for id , age , usertype
id  = int(input("enter id: "))
age= int(input("enter age: "))
usertype = input("enter usertype: ")

#-> if id is positive print valid id , if not print invalid id
if id > 0:
    print("Valid Id")
else:
    print("Invalid id")

#if age is greater than 18 print valid age else print invalid age
if age> 18:
    print("Valid Age")
else:
    print("Invalid Age")

#if usertype is "admin" print valid usertype else print invalid usertype
if usertype=="admin":
    print("Valid usertype")
else:
    print("Invalid usertype")


