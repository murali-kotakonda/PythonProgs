
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

