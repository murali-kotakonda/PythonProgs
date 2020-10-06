"""
//take input for id , age , usertype
//validate id & age , usertype
//if id is positive print valid id , if not print invalid id
//if age is greater than 18 print valid age else print invalid age
//if usertype is "admin" print valid usertype else print invalid usertype

if id is valid then only validate the age [ when age is invalid dont validate further ]
if age is valid then only validate the usertype

there is a dependency between the consitions
solution:
nested if statements. [ if inside a if]

"""

#input
id =  int(input("enter id "))
age =  int(input("enter age "))
usertype = input("enter usertype ")

if id >0 :
    print("valid id")
    if (age > 18):
        print("valid age") # two tabs here
        if (usertype == "admin"):
            print("valid usertype") # three tabs here
        else:
            print("invalid usertype")# three tabs here
    else:
        print("invalid age") # two tabs here
else:
    print("invalid id")





