"""
Custom Exception or use defined exception:
-----------------------------------------------
This is required for hanndling negative scenarios in the application.
ex:
if age <18  ====> which exception should We use from python ? None ; hence we hav to create our own exception class


1.Dev will create exeception class
2.dev will raise exception
3.dev will handle the exception


syntax for creating custom Exception class:
------------------------------------------
1.create a class that inherits Exception
2.provide constructor ;
    from child constructor call parent constructor

Req:
if id is negative or age is less than 18 throw exception
"""
class ServiceException(Exception):

    def __init__(self, errorCode, errorMsg):
        Exception.__init__(self,errorMsg)
        self.errorCode = errorCode
        self.errorMsg = errorMsg
        
#Here ServiceException is the custom exception class with errorCode, errorMsg  as instance variables
def validate(id, age):
    if id < 0:
        raise ServiceException("erro1", "Invalid id " + str(id))
    if age < 18:
        raise ServiceException("erro2", "Invalid age" + str(age))
    print("validation success")

try:
    validate(10,11)
except ServiceException as obj:
        print("invalid data for :: ",obj)
else:
    print("VALID DATA") 