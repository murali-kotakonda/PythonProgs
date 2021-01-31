"""
Custom Exception or use defined exception:
-----------------------------------------------

why should a dev create exception?
This is required for handling negative scenarios in the application.

ex:
if age <18
this is valid for python
but invalid for our project.

which exception obj we need to create for negative scenarios?
-> we should not use inbuilt exception.
-> create our own exception class and use class for obj creation.

age <18
====> which exception should We use from python ? None ;
===> hence we hav to create our own exception class

steps:
--------------------
1.Dev will create exception class
2.dev will raise exception
3.dev will handle the exception

exception class : any class which is a child of Exception is termed as exception class

syntax for creating custom Exception class:
------------------------------------------
1.create a class that inherits Exception
2.provide constructor ;
    from child constructor call parent constructor


ex1:
class ServiceException(Exception):

    def __init__(self, errorCode, errorMsg):
        Exception.__init__(self,errorMsg)
        self.errorCode = errorCode
        self.errorMsg = errorMsg

  raise ServiceException("erro1", "Negative numbers not allowed")

ex2:
class MyException(Exception):

    def __init__(self, errorMsg):
        Exception.__init__(self)
        self.errorMsg = errorMsg

raise MyException("age caanot be less then 18")


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