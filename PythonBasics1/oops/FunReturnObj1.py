def show(pObj):
    print(pObj.id)
    print(pObj.name)
    print(pObj.age)


class person:
    id=None
    name=None
    age=None

p1=person()
p2=person()
p3=person()

p1.id=1
p1.name='raju'
p1.age=23

p2.id=2
p2.name='kiran'
p2.age=25

p3.id=3
p3.name='ripesh'
p3.age=26

show(p1)
show(p2)
show(p3)