
def div(n1,n2):
    if n2==0:
        raise ArithmeticError("NUM2 cannot be zero")
    print(n1/n2)
    
try:
    div(6,0)
except ArithmeticError as Obj:
    print("invalid input due to ",Obj)

print("bye bye")



