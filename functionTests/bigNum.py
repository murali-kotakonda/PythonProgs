def biggerNum(num1, num2):
    if num1 > num2:
        return num1
    else: 
        return num2

 
def small(num1, num2):
    if num1 < num2:
        return num1
    else: 
        return num2

 
def test():
    a = int(input("enter num1"))
    b = int(input("enter num1"))
 
    big = biggerNum(a, b)
    print(big)
 
    big = biggerNum(100, 200)
    print(big)
