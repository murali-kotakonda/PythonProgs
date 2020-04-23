#call a function

# caller ---> decorator 
#
#without decorator   caller  ---> function ----> caller
#with decorator     caller -> decorator -> funtion --> decortor --> caller


# decorator will decode whether to call functn or not
# a)    if decortore decides to procced decoratir---- > funtcion
#       function ----> decorator
#       decorator ----> caller
# b)    if decortore decides to deny  decoratir---- > caller
 

def checkNegative(func):
    def operation(n1,n2):
        if n1<0 or n2 <0:
           return "numbers cannot be negative, cannot call the function"
        return func(n1,n2)
    return operation;


@checkNegative
def sum(n1,n2):
    return n1+n2

@checkNegative
def sub(n1,n2):
    return n1-n2

@checkNegative
def mul(n1,n2):
    return n1*n2

@checkNegative
def div(n1,n2):
    return n1/n2


print(sum(-20,20))
print(sub(20,20))
print(mul(-20,20))
print(div(20,20))