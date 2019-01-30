class Person:
    def __init__(self,id,name,age): #instance varibales
        self.id=id
        self.name=name
        self.age=age
        
p = Person(1000,"user1",67)
p1 = Person(1100,"user8",23)

# change obj data
p.id= 1200
p.name="user2"
p.age= 45


# print obj data
print("************p data************")
print(p.id)
print(p.name)
print(p.age)


# print obj data
print("************p1 data************")
print(p1.id)
print(p1.name)
print(p1.age)


