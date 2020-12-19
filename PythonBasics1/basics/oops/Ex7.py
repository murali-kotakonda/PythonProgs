"""

create a class with id, anme , age as instance variables.
create 3 objs , set data by taking input from console and display



"""

#write a function that takes obj as input arg
def display(pObj):
    print(pObj.id)
    print(pObj.name)
    print(pObj.age)

#write a function that returns person obj
def getObj():
    pObj = Person()
    pObj.id = int(input("enter id"))
    pObj.name = input("enter name")
    pObj.age = int(input("enter age"))
    return pObj


#create a class
class Person:
    id=None
    age= None
    name=None

    def show(self):
        print("Hello")


#create object
p1 = getObj()

p2 = getObj()

p3 = getObj()

#dispaly
print("****************show p1**********************")
display(p1)


print("****************show p2**********************")
display(p2)

print("****************show p3**********************")
display(p3)


print("****************show p4**********************")
p4= getObj()
display(p4)