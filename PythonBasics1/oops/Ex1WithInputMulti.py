class Person:
    # instance variables
    id = None
    name = None
    age = None

    # instance funtion
    def show(self):
        print("hello inside show")

count = int(input("enter no of persons"))

for i in range(count):
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

