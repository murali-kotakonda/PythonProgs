# seperate except for every error
intNum = 0
arr = [1, 2, 3, 4, 7]
try:
    intNum = int("1")
    print(arr[2])
    print(1/1)
except ValueError as obj:
    print("ValueError Argument", obj)
except IndexError :
    print("IndexError error ...")
except ArithmeticError:
    print("ArithmeticError error invalid usage of arguments...")
else:
   print("No Exception.......")
