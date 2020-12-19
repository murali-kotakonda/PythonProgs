#pass by value [ int,float, string, boolean, complex ]
def change(z):
    print("input =",z)
    z=100
    return z


x = 45

print(x)

x = change(x) # value of x is assigned to z

print(x)
