
"""
take input for id,name,age.
and keep data inside the obj
print the data

"""


class Person:
    # instance variables
    id = None
    name = None
    age = None

    # instance funtion
    def show(self):
        print("hello inside show")


# Syntax for obj creation
p1 = Person()

# Set data
p1.id = int(input("enter id"))
p1.name = input("enter name")
p1.age = int(input("enter age"))

# display data
print(p1.id)
print(p1.name)
print(p1.age)

# calling the function
p1.show()
