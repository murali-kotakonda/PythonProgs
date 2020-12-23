x=90
y=x
print(x,y)
y=89
print(x,y)


class Person:
    id = None
    name = None
    age = None


# create obj with data
p1 = Person()
p1.id = 1000
p1.name = "user1"
p1.age = 23

p2 = p1

print("************ P1 BEFORE *****************")
print(p1.id, p1.name, p1.age)


print("************ P2 BEFORE *****************")
print(p2.id, p2.name, p2.age)

p2.id=3000
p2.name="user4"
p2.age=30


print("************ P1 AFTER *****************")
print(p1.id, p1.name, p1.age)


print("************ P2 AFTER *****************")
print(p2.id, p2.name, p2.age)
