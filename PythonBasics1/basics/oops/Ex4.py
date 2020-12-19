"""

create a class with id, anme , age as instance variables.
create 3 objs , set data and display
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
print(p1.id)
print(p1.name)
print(p1.age)


print("****************show p2**********************")
print(p2.id)
print(p2.name)
print(p2.age)

print("****************show p3**********************")
print(p3.id)
print(p3.name)
print(p3.age)