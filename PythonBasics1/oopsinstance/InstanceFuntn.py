#self is a default argument ; and no need to pass value for self
# self is a default argument for every instance function
# self being 1st argument is mandatory

"""

Ex:
create obj , set data and display for perosn id,name,age
"""

class Person:

    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def show(self):
        print(self.id)
        print(self.name)
        print(self.age)


# Person is class
# id,name,age are instance variables
# __init__ is the constructr
# show is instance function
# self refers to the calling object

# create object and set data
p = Person(1200, "kumar", 45)

# print data - approch1
print("*******************************************************")
print(p.id)
print(p.name)
print(p.age)

# print data - approach2
print("*******************************************************")
p.show()  # calling instance function for printing the object data
#if show function is called using p , then logic of show function is applied on data of "p"


# create object and set data
print("***********************Show p1********************************")
p1 = Person(1300, "kumar123", 34)
p1.show()
#if show function is called using p1 object  , then logic of show function is applied on data of "p1"




# create object and set data
print("***********************Show p2********************************")
p2 = Person(2100, "raj", 25)
p2.show()
#if show function is called using p2 object  , then logic of show function is applied on data of "p2"


















# when show() funtn is called using p1 , then the logic inside the show() funtion is applied on the p1's data. self = p
# when show() funtn is called using p2 , then the logic inside the show() funtion is applied on the p2's data. self= p2


"""
p1.show2(10) #self = p1 , x=10
p2.show2(20) # self=p2 , x =20
"""