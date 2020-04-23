def div(n1,n2):
    if n2==0:
        myEx = ArithmeticError("NUM2 cannot be zero")
        raise myEx
    print(n1/n2)
    

div(6,0)
print("bye")





