
try:
    age  =  int ( input("enter age") )
    print("after concerting age= ",age)
except ValueError as ex:
    print("conversion not possible")

print("end")