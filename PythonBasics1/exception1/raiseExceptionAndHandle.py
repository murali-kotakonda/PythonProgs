
def div(n1,n2):
    if n2==0:
        raise ArithmeticError("NUM2 cannot be zero")
    print(n1/n2)



try:
    div(6, 2)
    div(6, 0)
    div(6, 3)
except ArithmeticError as Obj:
    print("invalid input due to ",Obj)

print("end")



