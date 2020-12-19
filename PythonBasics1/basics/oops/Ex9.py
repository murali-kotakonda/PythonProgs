#pass by value [ int,float, string, boolean, complex ]
def change(z):
    print("input =",z)
    z=100


x = 45

print(x)

change(x) # value of x is assigned to z

print(x)
