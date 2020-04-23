class Person:
    id = None
    name = None
    age = None


def show(pObj):
    print("*****************PRINTNG DATA*********************")
    print(pObj.id)
    print(pObj.name)
    print(pObj.age)


def getObj(pid, pname, page):
    pObj = Person()
    pObj.id = pid
    pObj.name = pname
    pObj.age = page
    return pObj


p1 = getObj(1, "raju", 23)
p2 = getObj(2, "kiran", 25)
p3 = getObj(3, "ram", 26)

show(p1)
show(p2)
show(p3)