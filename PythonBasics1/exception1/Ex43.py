"""
write common exception handling for ValueError,IndexError,ArithmeticError
for ValueError,IndexError,ArithmeticError --> print "Client error"
for any other exception --> print "Server error"

Req:
when we have common exception handling for different execption
how can we group it

"""

list = [1, 2, 3]

x= 50
y =0


try:
    print(list[2])
    print(list[8])  # trying to access 8th element but list has 3 elements

    divRes = x / y
    print("result = ", divRes)

    age = int(input("enter age"))
    print("after concerting age= ", age)

except (IndexError,ZeroDivisionError,ValueError) as ex: # executed when there is an exception
    print("Client error")
except Exception as ex: # executed when there is an exception
    print("Server error")

else:
    print("all operations success")

print("end")




