"""
take id ,age , usertype as input
perform validation
if id,age,usertype is valid ==> print valid data
if any data found to be invalid ==> print invalid data


id should be positive:
age should be greater than 18:
usertype should be "admin":



can we write multiple conditions in oen if statement?
YES

using [and]  [or]

if multiple conditions are joined using [AND] then the if block is executed if all conditions are satisfied.
if multiple conditions are joined using [OR] then the if block is executed if atleast one condition is satisfied.


"""
id = int(input("enter user id "))
age = int(input("enter user age"))
type = input("enter user type")


#approach1 Using and
if (id>0  and age>18 and type== 'admin' ):
    print("Valid data")
else:
    print("Invalid data")

#approach2 Using or
if (id<0  or age<18 or type!= 'admin' ):
    print("Invalid data")
else:
    print("Valid data")