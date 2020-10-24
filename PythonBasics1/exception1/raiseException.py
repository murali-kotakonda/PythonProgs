"""

can a dev create exception?
YES

STEPS:
1.Create exception obj
2.raise the exception

syntax:

ex = ArithmeticError("NUM2 cannot be zero")
raise ex



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






