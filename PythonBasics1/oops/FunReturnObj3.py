class Person:
    id = None
    name = None
    age = None


def show(pObj):
    print("*****************PRINTNG DATA*********************")
    print(pObj.id)
    print(pObj.name)
    print(pObj.age)


def getObjWithInput():
    pObj= Person()
    pObj.id = input("enter id")
    pObj.name = input("enter name")
    pObj.age = input("enter age")
    return pObj



p1 = getObjWithInput()
p2 = getObjWithInput()
p3 = getObjWithInput()

show(p1)
show(p2)
show(p3)




