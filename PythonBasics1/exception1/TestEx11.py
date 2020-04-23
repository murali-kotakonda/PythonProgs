# Program to depict else clause with try-except 
  
# Function which returns a/b 

#In python, you can also use else clause on try-except block which must be present after all the except clauses. The code enters the else block only if the try clause 
#does not raise an exception.
def div(a , b): 
    try: 
        c = a/b
    except ZeroDivisionError: 
        print("a/b result in 0")
    else: 
        print(c) 
  
# Driver program to test above function 
div(2.0, 3.0) 
div(3.0, 3.0)
 