def log(func):
    def operation():
         print("funtion start "+ str(func.__name__))
         func()
         print("funtion end " + str(func.__name__))
    return operation;

@log
def sum():
    print("helllo Im inside sum")

@log
def sub():
    print("helllo Im inside sub")

sum()
sub()