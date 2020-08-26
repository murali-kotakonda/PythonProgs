# seperate except fro every error
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


#group all exceptions
intNum = 0
arr = [1, 2, 3, 4, 7]
try:
    intNum = int("1")
    print(arr[2])
    print(1/1)
except(ValueError,IndexError,ArithmeticError) as obj:
  print("Invalid access to components.",obj)
else:
  print("No Exception.......")   


#global exception    
intNum = 0
arr = [1, 2, 3, 4, 7]
try:
    intNum = int("1")
    print(arr[2])
    print(1/1)
except(Exception) as obj:
    print("Invalid access to components.",obj)
else:
    print("No Exception.......")

    