"""

create a class with id, anme , age as instance variables.
create 3 objs , set data and display.

simplify the display logic for objects.

solution:
write a function that takes object as input argument  for dispalying thge obj data
"""

#write a function that takes obj as input arg
def display(pObj):
    print(pObj.id)
    print(pObj.name)
    print(pObj.age)

#create a class
class Person:
    id=None
    age= None
    name=None

    def show(self):
        print("Hello")


#create object
p1 = Person()
p2 = Person()
p3 = Person()

# set data
p1.id = 90
p1.name="kumar"
p1.age = 45

# set data
p2.id = 9000
p2.name="raj"
p2.age = 45


# set data
p3.id = 90101
p3.name="ram"
p3.age = 54

#dispaly
print("****************show p1**********************")
display(p1)


print("****************show p2**********************")
display(p2)

print("****************show p3**********************")
display(p3)