
arr = [1, 2, 3, 4, 7]


def square():
    intNum = 0
    try:
        intNum = int("1");
        print(arr[2])
        print(1/1)
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

    
square()








try :  
    a = 3
    if a < 4 : 
  
        # throws ZeroDivisionError for a = 3  
        b = a/(a-3) 
      
    # throws NameError if a >= 4 
    print("Value of b = ", b) 
  
# note that braces () are necessary here for multiple exceptions 
except(ZeroDivisionError, NameError): 
    print("\nError Occurred and Handled")