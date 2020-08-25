import copy

class Person:
    def __init__(self,id,name,age): #instance varibales
        self.id=id
        self.name=name
        self.age=age

p1 = Person(1000,"user1",67)

#p2 =p1  #new object is not created
p2 = copy.copy(p1) #new object is createdwith data from old obj

print(p1.id,p1.name,p1.age)
print(p2.id,p2.name,p2.age)

p2.id=9000
p2.name ="shyam"
p2.age=34

print("*************changer p2*********************")
print(p1.id,p1.name,p1.age)
print(p2.id,p2.name,p2.age)


