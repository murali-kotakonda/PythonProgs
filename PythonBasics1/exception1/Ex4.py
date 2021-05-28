"""
can we write try with multiple except blocks?
Yes

at a time only one except block is executed.

For IndexError ,ZeroDivisionError ,ValueError

we need to write 3 except blocks

"""

list = [1, 2, 3]

x = 50
y = 0

age =None


try:
    print(list[0])
    print(list[7])  # trying to access 8th element but list has 4 elements

    divRes = x / y
    print("result = ", divRes)

    age  =  int(input("enter age") )
    print("after concerting age= ",age)
except IndexError as ex:
    print("invalid index please try again")
except ZeroDivisionError as ex:
    print("denominator cannot be zero. Please correct ")
except ValueError as ex:
    print("Please enter only digits for age")
else:
    print("No exception")

