# global variables
n1 = 56

def printLarge(a,b):
    if a>b:
        print("bigger = ",a)
    else:
        print("bigger = ",b)
        
def printSmall(a,b):
    if a>b:
        print("small = ",b)
    else:
        print("small = ",a)        




def test():
    printLarge(20,30)
    n1= int(input("enter num1"))
    n2= int(input("enter num2"))
    printLarge(n1,n2)

print("hi")