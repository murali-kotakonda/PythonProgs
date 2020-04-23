def f2(name):
    print("input =", name)

f2(12)
f2("user1")
f2(1213.78)
f2(True)

#sum of two nums
def sum(x, y):
    z = x + y
    print("sum = ", z)

sum(30, 20)

a = 40
b = 90
sum(a, b)

n1 = int(input("enter n1"))
n2 = int(input("enter n1"))
sum(n1, n2)

#find big of two nums
def findLarge(a,b):
    if a>b:
        print("bigger is", a)
    else:
         print("bigger is", b)
    
findLarge(10,20)
findLarge(50,20)


def div(x,y):
    if(y == 0):
        print("division not possible")
    else:
        print(x/y)

div(10,2)
div(18.4,3)
div(9,0)
div(10.7,9.0)
