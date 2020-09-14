"""

write common exception handling for ValueError,IndexError,ArithmeticError

"""
arr = [1, 2, 3, 4, 7]


def square():
    intNum = 0
    try:
        intNum = int("1");
        print(arr[2])
        print(1/1)
    except (ValueError,IndexError,ArithmeticError):
            print("error invalid usage of arguments...")
    else:
        print("No Exception.......")

    
square()







