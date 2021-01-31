
# take name and pass as input , 
#if name == 'admin' and  pass ='admin' login success else login failure
name = input("enter name")
password = input("enter pass")
 
if name in ["hyd","chennai"]:
    print("ser provided")
      
# logical and ---> execute the if statement if both conditions are satisfied
if name == 'admin' and password == 'admin' :
    print("Login success")
else:
     print("Login failure")

# logical or ---> execute the if statement if atleast one condition is satisfied
# if the input userType = 'admin' or 'agent' ---> provide access if not dont provide
userType = input("enter userType")
if userType == 'admin' or userType == 'agent':
    print("grant access")
else:
     print("access denied")


# if the usertype is not admin:---> create security incident 
if not(userType == 'admin') :
     print("created security incident")


#example on not

