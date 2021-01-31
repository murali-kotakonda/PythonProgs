"""
while loop
take names continuously and if the name value is "END"  end the program.
"""

data =""

str = ""
while(data != "END"):
     data = input("enter name : ")
     str= str+ " "+ data

print("your names are : ", str )