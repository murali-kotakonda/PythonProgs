
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
