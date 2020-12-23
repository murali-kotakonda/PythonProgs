"""
#create 3 objs , set data and show data
simplify logic for create the obj and set the data

solution:
write a function that takes id,name ,age as input args and retuns obj 

"""

def show(pObj):
    print(pObj.id)
    print(pObj.name)
    print(pObj.age)


# function that retuns obj
def create(pId, pName, pAge):
    # create obj
    pObj = person()

    # set the data
    pObj.id = pId
    pObj.name = pName
    pObj.age = pAge

    return pObj  # return obj


class person:
    id = None
    name = None
    age = None


# create object
print("************** show p1 *************************")
p1 = create(1, 'raju', 23)
show(p1)  # then pObj will be p1

print("************** show p2 *************************")
p2 = create(2, 'kiran', 25)
show(p2)  # then pObj will be p2

print("************** show p3 *************************")
p3 = create(3, 'ripesh', 26)
show(p3)  # then pObj will be p3

