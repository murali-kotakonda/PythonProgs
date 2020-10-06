"""
//take input for id , age , usertype
//validate id & age , usertype
//if id is positive print valid id , if not print invalid id
//if age is greater than 18 print valid age else print invalid age
//if usertype is "admin" print valid usertype else print invalid usertype

if id is valid then only validate the age [ when age is invalid dont validate further ]
if age is valid then only validate the usertype

there is a dependency between the conditions
solution:
if and elif

when should we use if and elif?
-> there is a dependency between the conditions
-> at a time only one block is executed

"""



#input
id =  int(input("enter id "))
age =  int(input("enter age "))
usertype = input("enter usertype ")

if id <0 :
    print("invalid id")
elif (age < 18):
    print("valid id")
    print("invalid age")
elif (usertype != "admin"):
    print("valid id")
    print("valid age")
    print("invalid usertype")
else:
    print("valid id")
    print("valid age")
    print("valid usertype")
