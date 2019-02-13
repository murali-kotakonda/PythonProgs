def checkNegative(func):
    def operation(n1,n2):
        if n1<0 or n2 <0:
            print("numbers cannot be negative")
            return
        return func(n1,n2)
    return operation;

def check(func):
    def operation(n1,n2):
        res = func(n1,n2)
        if res < 0:
            print("unexpected negative number")
        return res;
    return operation;
 
@checkNegative
@check
def sum(n1,n2):
    return n1+n2

@checkNegative
@check
def sub(n1,n2):
    return n1-n2

@checkNegative
@check
def mul(n1,n2):
    return n1*n2

@checkNegative
def div(n1,n2):
    return n1/n2


print(sum(20,20))
print(sub(20,40))
print(mul(20,20))
print(div(20,20))