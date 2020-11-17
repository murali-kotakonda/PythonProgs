"""
 Perform validation
 print "numbers cannot be negative "if n1 or n2 is < 0

if the result is< 0
print("unexpected result , result cannot be number")

"""


def checkNegative(func):  #pre check
    def operation(n1,n2):
        if n1<0 or n2 <0:
            print("numbers cannot be negative")
            return
        return func(n1,n2)
    return operation;

def checkRes(func): #post check
    def operation(n1,n2):
        res = func(n1,n2)
        if res < 0:
            return("unexpected result , result cannot be number")
        return res
    return operation
 
@checkNegative
@checkRes
def sum(n1,n2):
    return n1+n2

@checkNegative
@checkRes
def sub(n1,n2):
    return n1-n2

@checkNegative
@checkRes
def mul(n1,n2):
    return n1*n2

@checkNegative
@checkRes
def div(n1,n2):
    return n1/n2

print(sum(20,20))
print(sub(20,40))
print(mul(20,20))
print(div(20,20))