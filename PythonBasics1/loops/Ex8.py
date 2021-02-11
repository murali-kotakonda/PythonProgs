"""
while loop
take names continuously and if the name value is "END"  end the program and print what are thge names entred so far.
"""

data =""
str = ""

while(data != "END"):
     data = input("enter name : ")
     str= str+ " "+ data

print("your names are : ", str )