"""
take id ,age , usertype as input
perform validation

id should be positive:
age should be greater than 18:
usertype should be "admin":

if id,age,usertype is valid ==> print valid data
if any data found to be invalid ==> print invalid data



can we write multiple conditions in oen if statement?
YES

using [and]  [or]

if multiple conditions are joined using [AND] then the if block is executed if all conditions are satisfied.
if multiple conditions are joined using [OR] then the if block is executed if atleast one condition is satisfied.


"""
id =  int(input("enter id "))
age =  int(input("enter age "))
usertype = input("enter usertype ")

if id >0 :
   if (age > 18):
       if (usertype == "admin"):
            print("valid usertype") # three tabs here
       else:
            print("invalid Data")# three tabs here
   else:
        print("invalid Data") # two tabs here
else:
    print("invalid Data")
