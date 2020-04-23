# create exception class
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
    validate(10,19)
except ServiceException as obj:
        print("invalid data for :: ",obj)
else:
    print("VALID DATA") 

print("end of code")