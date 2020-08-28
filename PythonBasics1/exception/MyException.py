# create exception class
"""
Custom exception / User Defined exception / Business Exception:
-- Required to handle the negative scenarios in the project

-Dev creates exception class
-Dev creates/raises execption
-Dev handles exception



How to create exception class:
-Every exception should be child class of "Exception"
- From constr call the constr of Exception class

#-Dev creates exception class
class ServiceException(Exception):

    def __init__(self, errorCode, errorMsg):
        Exception.__init__(self)    #from constr call the constr of Exception class
        self.errorCode = errorCode
        self.errorMsg = errorMsg


#Dev creates/raises execption obj
def validate():
	myObj = ServiceException("erro1", "Invalid id "))
	raise myObj

#Dev handles exception
try:
    validate()
except ServiceException as obj:
        print("invalid data for :: ",obj)

if id <0 or age < 18 create the exception
"""


class ServiceException(Exception):

    def __init__(self, errorCode, errorMsg):
        Exception.__init__(self)
        self.errorCode = errorCode
        self.errorMsg = errorMsg


# raise exception
def validate(id, age):
    if id < 0:
        myObj = ServiceException("erro1", "Invalid id " + str(id))
        raise myObj
    if age < 18:
        myObj = ServiceException("erro2", "Invalid age" + str(age))
        raise myObj


# call validate funtn and handle exception
try:
    validate(-1, 19)
except ServiceException as obj:
    print("invalid data for :: ", obj.errorMsg)
else:
    print("VALID DATA")

print("end of code")
