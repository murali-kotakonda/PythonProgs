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

#if we pass the primitive data int, float , str  to the funtion and if the funtion modofies the values , it will not have any impact to the caller
#if we pass the object to the funtion and if the funtion modifies the obj data , it will  have any impact to the caller

