id=int(input("enter your inputs"))
age=int(input("enter your inputs"))

usertype=input("enter your inputs")

if id>=0:
    print("valid id ")
else:
    print("invalid id")

if age>18:
    print ("age met the conditions")
else:
    print("age not met the condition")

if usertype=="admin":
    print("valid usertype")
else:
    print("invalid usertype")

print("end pgm")