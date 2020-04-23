# Create exception CLASS
class MyException(Exception):

    def __init__(self, errorCode, errorMsg):
        Exception.__init__(self)
        self.errorCode = errorCode
        self.errorMsg = errorMsg


# raise exception if input is < 0

def f1(n):
    if n < 0:
        raise MyException("erro1", "Negative numbers not allowed")
    print("result", n * 2)


# handle exception
try:
    f1(1)
    f1(-10)
except MyException as ex:
    print("failed execution due to ", ex.errorMsg)
else:
    print("success")


