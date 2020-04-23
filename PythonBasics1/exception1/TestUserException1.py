import logging

class ServiceException(Exception):

    def __init__(self, errorCode, errorMsg):
        Exception.__init__(self)
        self.errorCode = errorCode
        self.errorMsg = errorMsg

class Person:
    id=None
    userType= None
    age= None

def validate(personInfo):
    if personInfo.id < 0:
        raise ServiceException("erro1", "Invalid id " + str(personInfo.id))
    if personInfo.age < 18:
        raise ServiceException("erro2", "Invalid age" + str(personInfo.age))
    if personInfo.userType!='admin' and personInfo.userType!='agent':
        raise ServiceException("erro3", "Invalid userType" + str(personInfo.userType))
    print("valid data . process sucess")

def captureInput():
    p = Person()
    p.id = int(input("enter id:"))
    p.age = int(input("enter age:"))
    p.userType = input("enter usertype:")
    return p

def save(p):
    print("saving person info")

def process():
    p = captureInput()
    validate(p)
    print("validation success")
    save(p)


try:
    process();
except ServiceException as ex:
    print("Validation failed due to :: " + ex.errorCode , " message  = ", ex.errorMsg)
except Exception as ex:
    print("Validation failed due to server issue:: ")

