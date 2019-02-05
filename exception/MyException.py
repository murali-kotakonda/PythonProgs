class ServiceException(Exception):

    def __init__(self, errorCode, errorMsg):
        Exception.__init__(self,errorMsg)
        self.errorCode = errorCode
        self.errorMsg = errorMsg
        

def validate(id, age):
    if id < 0:
        raise ServiceException("erro1", "Invalid id " + str(id))
    if age < 18:
        raise ServiceException("erro2", "Invalid age" + str(age))

try:
    validate(10,11)
except ServiceException as obj:
        print("invalid data for :: ",obj)
else:
    print("VALID DATA") 