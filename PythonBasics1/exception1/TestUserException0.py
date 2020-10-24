# Create exception CLASS
class MyException(Exception):

    def __init__(self, errorCode, errorMsg):
        Exception.__init__(self)
        self.errorCode = errorCode
        self.errorMsg = errorMsg




#raise exception
def square(num):
    if num<0:
        raise MyException("erro1", "Negative numbers not allowed")
    print("square =" , num*num)



try:
    num1 = int(input("enter num"))
    square(num1)
except MyException as ex:
    print("operation failed due to ", ex.errorMsg)
else:
    print("operation success")
