


"""
write a print statement for every method start
write a print statement for every method end
"""

def log(func):
    def operation():
         print("funtion start "+ str(func.__name__))
         func()
         print("funtion end " + str(func.__name__))
    return operation;

@log
def sum():
     print("In sum")


@log
def sub():
    print("In sub")

sum()
sub()