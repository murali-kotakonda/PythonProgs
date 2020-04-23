
c = 40
d = c  # copying value of c to d
print(d)

d = 50
print(c)
print(d)

# purpose is 
c = 60
d = 60
print(c is d)

e = d
print(e is d)
e = 90

print(e is d)
print(e is not d)
