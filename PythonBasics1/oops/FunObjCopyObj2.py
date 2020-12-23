"""
Copy object
assign the OBJ/ref variable to another variable
"""


class person:
    id = None
    name = None
    age = None


# create p1 object
p1 = person()  # new obj is created

p1.id = 1
p1.name = 'raju'
p1.age = 23

# copy
p2 = p1  # No new obj is created
# both p1 and p2 are pointing to same object
# when we change p1 , p2 also changes
# when we change p2 , p1 also changes

print("************** show p1 *************************")
print(p1.id)
print(p1.name)
print(p1.age)

print("************** show p2 *************************")
print(p2.id)
print(p2.name)
print(p2.age)

# change p2
p2.id = 9000
p2.name = "user3"
p2.age = 34

print("************** show p1 *************************")
print(p1.id)
print(p1.name)
print(p1.age)

print("************** show p2 *************************")
print(p2.id)
print(p2.name)
print(p2.age)





