# Class
class Person:
    id = None
    name = None
    age = None


# global funtion
def getObj(pid, pname, page):
    pObj = Person()
    pObj.id = pid
    pObj.name = pname
    pObj.age = page
    return pObj


# create obj for p1 with data
p1 = getObj(1, "raju", 23)  # new obj is created

# assign p1 to p2
p2 = p1  # no new obj created

print(" BEFORE CHANGING ")
print(p1.id, p1.name, p1.age)
print(p2.id, p2.name, p2.age)

p2.id = 9000
p2.name = "user3"
p2.age = 34

print(" AFTER CHANGING ")
print(p1.id, p1.name, p1.age)
print(p2.id, p2.name, p2.age)







