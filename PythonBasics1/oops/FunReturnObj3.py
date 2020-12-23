
"""
#create 3 objs , set data by taking input from console and show data

simplify logic for create the obj and set the data+ print data

solution:
write a function that takes id,name ,age as input args and retuns obj


"""

def show(pObj):
    print(pObj.id)
    print(pObj.name)
    print(pObj.age)


# function that retuns obj
# function that retuns obj
def create():
    # create obj
    pObj = person()

    # set data by taking input from console
    pObj.id = int(input("enter id"))
    pObj.name = input("enter name")
    pObj.age = int(input("enter age"))

    return pObj  # return obj

class person:
    id = None
    name = None
    age = None


# create object
print("************** show p1 *************************")
p1 = create()
show(p1)  # then pObj will be p1

print("************** show p2 *************************")
p2 = create()
show(p2)  # then pObj will be p2

print("************** show p3 *************************")
p3 = create()
show(p3)  # then pObj will be p3

