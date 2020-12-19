"""

create a class with id, anme , age as instance variables.
create obj , set data and display
"""

#create a class
class Person:
    id=None
    age= None
    name=None

    def show(self):
        print("Hello")


#create object
p1 = Person()

# set data
p1.id = 90
p1.name="kumar"
p1.age = 45

#dispaly
print(p1.id)
print(p1.name)
print(p1.age)