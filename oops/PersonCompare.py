class Person:
    def __init__(self,id,name,age): #instance varibales
        self.id=id
        self.name=name
        self.age=age
    
    def __eq__(self, other): 
        return self.id == other.id and self.name == other.name
        

p = Person(1000,"user1",67)
p1 =Person(1000,"user1",67)

p2 =Person(1000,"user1",68)

if p==p1:
    print("p and p1 are duplicates")
else:
    print("p and p1 are not duplicates")

print(p1==p2)    



