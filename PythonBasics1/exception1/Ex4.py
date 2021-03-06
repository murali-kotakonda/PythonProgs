"""
IndexError
ZeroDivisionError
ValueError

we need to write 3 except blocks 

"""

list = [1, 2, 3]

x = 50
y = 0

age =None
try:
    print(list[2])
    print(list[9])

    divRes = x / y

    age = int(input("enter age"))
    print("after concerting age= ", age)
except IndexError as ex:
    print("exception occured , please use the correct index ")

except ZeroDivisionError as ex:
    print("division by zero not possible")

except ValueError as ex:
    print("enter a valid number")

else:
    print("No exception")
