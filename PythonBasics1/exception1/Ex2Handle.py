divRes =-1;
try:
    x= 50
    y =1
    divRes = x/y
except ZeroDivisionError as ex:
    print("denominator cannot be zero")

print("result = ", divRes)# ZeroDivisionError