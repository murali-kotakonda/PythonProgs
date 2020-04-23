
age  =  int ( input("enter age") )
print("after concerting age= " ,age)  # ValueError



try:
    age  =  int ( input("enter age") )
    print("after concerting age= " ,age)  # ValueError
except ValueError as ex:
    print("please enter age in numbers..."  )# msg to customer
    print(ex) # info to be written un server logs
print("prog ends")




