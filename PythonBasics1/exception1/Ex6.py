
#group all exceptions
intNum = 0
arr = [1, 2, 3, 4, 7]
try:
    intNum = int("1")
    print(arr[2])
    print(1/1)
except(ValueError,IndexError,ArithmeticError) as obj:
    print("Client error ",obj)
except Exception as ex:
    print("Server error ", ex)
else:
    print("No Exception.......")

