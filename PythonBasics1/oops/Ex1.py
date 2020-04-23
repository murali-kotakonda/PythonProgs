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
p1.id = 30000
p1.name = "user1"
p1.age = 45

# display data
print(p1.id)
print(p1.name)
print(p1.age)

#calling the function
p1.show()
