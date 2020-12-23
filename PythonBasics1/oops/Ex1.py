"""
Object oriented programming:
---------------------------------------------

->Programming style that defines the common rules , regulations,standards , guidelines
for writing better programming


-> ex: java, .net , python , php , groovy ,go , php , javascript , anagular js

Topics:
-> class, object , enapsulation , abstraction , inheritance



 Class
--------------------------
-> Userdefined datatype
-> Class is used to represent the real time entities/structure/model.
ex: Company, Branch , Dep, sub-dept, Project , Employee ,
-> Class doesnt contain any data.
-> class is created before run-time
->class is a logical representation
->class is a template


Class has:
 -> instance variables
 -> instance funtions


global varibles:   <globla area>
local varibles:    < inside the function>
instance variables : < inside the class>


"""

x = 90


def process():
    y = 89
    print("process")


class Person:
    # instance variables
    id = None
    name = None
    age = None

    # instance funtion
    # every instance function has self as default arg
    def show(self):
        print("hello inside show")


"""
 here x is a global variable
y is a local variable
process() is a global function
show(self): is a instance function
 """


# Syntax for obj creation
p1 = Person()

# Set data
p1.id = 30000
p1.name = "user1"
p1.age = 45

# display data
print(p1.id)
print(p1.name)
print(p1.age)

#calling the function
p1.show()
