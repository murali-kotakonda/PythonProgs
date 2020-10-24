# try with multiple except blocks
# at a time only one except block is executed
list = [1, 2, 3]

x= 50
y =1


try:
    print(list[2])
    print(list[1])  # trying to access 8th element but list has 3 elements

    divRes = x / y
    print("result = ", divRes)

    age = int(input("enter age"))
    print("after concerting age= ", age)

except IndexError as ex: # executed when there is an exception
    print("list operation failed.")
    print("Invalid access to list")
except ZeroDivisionError as ex:
    print("division failure")
    print("division by zero not possible")
except ValueError as ex:
    print("conversion not possible")
else:
    print("all operations success")

print("end")