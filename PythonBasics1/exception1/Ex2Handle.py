x= 50
y =2

try:
    divRes = x/y
    print("result = ", divRes)
except ZeroDivisionError as ex:
    print("division failure")
    print("division by zero not possible")
else:
    print("division success")

print("end")