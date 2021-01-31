import copy
"""
How to create the copy of an obj?
create a new obj with data from other obj ; but both are independent

 
solution:
import copy


use copy.copy() function



COPY OBJECT:
-------------------
import copy

p1 = Person(1000, "user1", 34)
p2 = copy.copy(p1)
p2 = copy.deepcopy(p1)

"""
class Person:
    def __init__(self,id,name,age): #instance varibales
        self.id=id
        self.name=name
        self.age=age


#create the obj with data
p1 = Person(1000,"user1",67)

#p2 =p1  #new object is not created
p2 = copy.copy(p1) #new object is created with data from old obj

print(p1.id,p1.name,p1.age)
print(p2.id,p2.name,p2.age)

p2.id=9000
p2.name ="shyam"
p2.age=34

print("*************change p2*********************")
print(p1.id,p1.name,p1.age)
print(p2.id,p2.name,p2.age)


