"""

create a class with id, anme , age as instance variables.
create 3 objs , set data and display.

simplify the create obj + set data

solution:
write a function that takes id,name , age as input arguments and returns person object

"""

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


#create a class
class Person:
    id=None
    age= None
    name=None

    def show(self):
        print("Hello")


#create object
p1 = getObj(90,"kumar",45)

p2 = getObj(9000,"raj",34)

p3 = getObj(90101,"ram",54)

#dispaly
print("****************show p1**********************")
display(p1)


print("****************show p2**********************")
display(p2)

print("****************show p3**********************")
display(p3)


print("****************show p4**********************")
p4= getObj(1200,"shyam",28)
display(p4)