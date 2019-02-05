def div(a , b): 
    try: 
        c = a/b
        print("*********")
    except ZeroDivisionError: 
        print("a/b result in 0")
    else: 
        print(c) 
  
# Driver program to test above function 
div(5,1) # try + else
div(4,0) # partial try + except