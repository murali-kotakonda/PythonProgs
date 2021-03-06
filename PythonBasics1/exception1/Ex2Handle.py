x= 50
y =0

try:
    divRes = x/y
    print("result = ", divRes)
except ZeroDivisionError as ex:
    print("division by zero not possible")
else:
    print("division success")


print("bye")

#python is creating ZeroDivisionError: division by zero