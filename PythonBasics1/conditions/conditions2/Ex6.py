"""
take id ,age , usertype as input
perform validation

id should be positive:
age should be greater than 18:
usertype should be "admin":

if id,age,usertype is valid ==> print valid data
if any data found to be invalid ==> print invalid data

Req:
can we write multiple conditions in one if statement?
Yes

- and
   if multiple conditions are joined using 'and' then the if block is executed only if all the conditions are satisfied
- or
   if multiple conditions are joined using 'OR' then the if block is executed if atleast one condition is satisfied

"""


#take input for id , age , usertype
id  = int(input("enter id: "))
age= int(input("enter age: "))
usertype = input("enter usertype: ")


#approach1
if id>0 and age>=18 and usertype=="admin":
     print("Valid data")
else:
    print("Invalid data")


#approach2
if id<0 or age<18 or usertype!="admin":
     print("Invalid data")
else:
    print("Valid data")



