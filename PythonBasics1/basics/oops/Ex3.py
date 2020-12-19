"""

create a class with id, anme , age as instance variables.
create obj , set data by taking input and display

mention the number of persons
take input for multiple persons ,
"""

#create a class
class Person:
    id=None
    age= None
    name=None

    def show(self):
        print("Hello")


size = int(input("Enter the number of persons"))


for i in range(size):
    #create object
    p1 = Person()


    # set data
    p1.id = int(input("enter id"))
    p1.name=input("enter name")
    p1.age = int(input("enter age"))

    #dispaly
    print(p1.id)
    print(p1.name)
    print(p1.age)

