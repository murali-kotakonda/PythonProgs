def f1(n):
    if n < 0:
        raise ArithmeticError("Negative numbers not allowed")
    print(n * 2)

f1(1)
    
try:   
    f1(-10)
except ArithmeticError as ex:
     print("failed execution due to ",ex)
else:
    print("success")