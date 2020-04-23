class Person:
    id=None
    name=None
    age=None

p=Person()
p1=Person()

p.id=2000
p.name="user1"
p.age=45

p1.id=2001
p1.name="user2"
p1.age=47

print(p.id)
print(p.name)
print(p.age)

print(p1.id)
print(p1.name)
print(p1.age)