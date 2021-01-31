"""

can a developer create exception?
YES


STEPS:
-----------------------
1.Create exception obj
2.raise the exception

#syntax for Create exception obj:
ex1 = ValueError("invalid data")
ex2 = IndexError("invalid index value")
ex3 = ArithmeticError("invalid arthmetic ")

#syntax for raise exception
raise ex1
raise ex2
raise ex3


Req: Perform div of two nums
if the second num is zero then throw exception
"""

def div(n1, n2):
    if n2 == 0:
        raise ArithmeticError("NUM2 cannot be zero")
    print(n1 / n2)


div(6,2)
div(6, 0)
div(6, 3)
print("end")






