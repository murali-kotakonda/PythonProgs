# take name and pass as input ,
#if name == 'admin' and  pass ='admin' login success else login failure

name = input("enter login  name : ")
password = input("enter password : ")


if name ==  "admin":
    if password =="admin":
        print("login succes")
    else:
        print("login failure")
else:
    print("login failure")
