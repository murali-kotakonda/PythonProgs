
arr = [1, 2, 3, 4, 7]


def square():
    intNum = 0
    try:
        intNum = int("a");
        print(arr[2])
        print(1/0)
#     #get execption obj
#     except ValueError as obj:
#         print("invalid Argument", str, obj)
    except (ValueError,IndexError,ArithmeticError) as obj:
            print("error invalid usage of arguments...",obj)
    else:
        print("No Exception.......")

    
square()







