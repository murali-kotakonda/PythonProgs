"""
#Debug :
trace the program at the run time

How to debug:
1.setup the break points
2.Run the prog in debug mode
and observe code flow and variable values.


"""


"""
//take input for id , age , usertype

//validate id & age , usertype
//if id is positive print valid id , if not print invalid id
//if age is greater than 18 print valid age else print invalid age
//if usertype is "admin" print valid usertype else print invalid usertype
"""

 

#take input for id , age , usertype
id = int(input("enter id :"))
age = int(input("enter age :"))
usertype = input("enter usertype :")


#if id is positive print valid id , if not print invalid id

if id >= 0:
    print("valid id")
else:
    print("invalid id")

#if age is greater than 18 print valid age else print invalid age

if age > 18 :
    print("valid age")
else:
    print("invalid age")

#if usertype is "admin" print valid usertype else print invalid usertype
if usertype == "admin":
    print("valid usertype")
else:
    print("invalid usertype")




