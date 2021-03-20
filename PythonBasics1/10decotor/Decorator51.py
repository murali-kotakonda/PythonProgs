


"""
write a print statement for every method start
write a print statement for every method end
"""

def log(func):
    def operation():
         print("funtion start "+ str(func.__name__))
         func()
         print("funtion end " + str(func.__name__))
    return operation

@log
def sum(x,y):
    r = x+y
    print(" sum = ",r)

@log
def sub(x,y):
    r = x - y
    print(" sub = ", r)

sum(40,20)
sub(30,20)