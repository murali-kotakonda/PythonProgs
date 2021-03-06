
class ServiceException(Exception):

    def __init__(self, errorCode, errorMsg):
        Exception.__init__(self,errorMsg)
        self.errorCode = errorCode
        self.errorMsg = errorMsg


def div(n1, n2):
    if n2 == 0:
        raise ServiceException("erro3","NUM2 cannot be zero")
    print(n1 / n2)


try:
    div(6,2)
    div(6, 0)
    div(6, 3)
except ServiceException as ex:
    print("issue due to ", ex)

print("end")