class Person:
    id = None
    name = None
    age = None


def change(pObj):  # take obj as input and modify the obj
    pObj.id = 9000
    pObj.name = "user2"
    pObj.age = 34


# create obj with data
p = Person()
p.id = 1000
p.name = "user1"
p.age = 23

print("************BEFORE*****************")
print(p.id, p.name, p.age)

change(p)  # call funtion and pass the obj

print("************AFTER*****************")
print(p.id, p.name, p.age)

