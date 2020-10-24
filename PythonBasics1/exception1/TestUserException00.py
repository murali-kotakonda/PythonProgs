# perform the square of num if input is < 0 raise exception
#when exception is created the only code that executes is the except block
#if input is invalid dont execute any logic, execute only the logic to print error message


# Create exception CLASS
class MyException(Exception):

    def __init__(self, errorCode, errorMsg):
        Exception.__init__(self)
        self.errorCode = errorCode
        self.errorMsg = errorMsg



#raise exception
def square(num):
    print("square function:start")
    if num<0:
        raise MyException("erro1", "Negative numbers not allowed")
    print("square =" , num*num)
    print("square function:end")

def validate(num):
    print("validate function:start")
    square(num)
    print("validate function:end")

def process(num):
    print("process function:start")
    validate(num)
    print("process function:end")

#main program
try:
    num1 = int(input("enter num"))
    process(num1)
except MyException as ex:
    print("operation failed due to ", ex.errorMsg)
else:
    print("operation success")

"""
main prog calls---> process(num) -----> validate(num)  ----> square(num)

where is exception created?
 square(num) funtion
 
where are we doing the exception handling?
 main prog 
 so write try and except in main prog
 
when exception is created in square() funtion , then control will directly gos to the execpt block of main prog


"""