# Pass by reference

#write a function that takes obj as input arg
def display(pObj):
    print(pObj.id)
    print(pObj.name)
    print(pObj.age)

#write a function that returns person obj
def getObj(id,name,age):
    pObj = Person()
    pObj.id = id
    pObj.name = name
    pObj.age = age
    return pObj


def change(pObj):  #pObj = p1, pObj and p1 are referring to same object
    pObj.id = 6790
    pObj.name = "ramesh"
    pObj.age = 56

class Person:
    id=None
    age= None
    name=None

#create obj + set data
p1 = getObj(90,"kumar",45)

#print obj
print("****************show p1**********************")
display(p1)


#call the change function by pasisng the object
change(p1) # assign p1 to pObj  , pObj = p1

print("****************show p1 aftr calling change function **********************")
display(p1)

"""
if you are passing a object to a function (ex:change()) and if the function modifies the object
then it will have impact to the caller

"""