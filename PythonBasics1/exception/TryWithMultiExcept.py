
arr = [1]

def process():
    intNum = 0
    try:
        intNum = int("3");
        print(arr[0])
        print(1/0)
#     #get execption obj
#     except ValueError as obj:
#         print("invalid Argument", str, obj)
    except ValueError:
        print("ValueError Argument")
    except IndexError :
            print("IndexError error ...")
    except ArithmeticError:
            print("ArithmeticError error invalid usage of arguments...")
    else:
        print("No Exception.......")

    print("end----")
    
process()
