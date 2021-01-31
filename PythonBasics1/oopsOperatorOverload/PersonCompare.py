class Person:
    def __init__(self,id,name,age): #instance varibales
        self.id=id
        self.name=name
        self.age=age

    def __eq__(self, other):  # self = p1 and other =p2
        return self.id == other.id and self.name == other.name and self.age == other.age
    #returns boolean


p2 = Person(1000,"user1",67)
p1 = Person(1000,"user1",67)

# internally calls __eq__
if p2==p1:
    print("p2 and p1 are duplicates")
else:
    print("p2 and p1 are not duplicates")



"""
by default  ==  compares the address of the objects


1.steps to be followed for == should compare the content :
solution:
provide __eq__ funtion inside the Person class
and write the compare logic inside the function.

summary:
if we want to compare two objects , 
the basic rule is the class has to provide the __eq__ funtion.

"""
















"""








p3=p1
if p3==p1:
    print("p3 and p1 are duplicates")
else:
    print("p3 and p1 are not duplicates")






p2 =Person(1000,"user1",68)

print(p1==p2)    zd
"""


# assignment:
#take multiple person objs and remove duplicates
# use list or set



