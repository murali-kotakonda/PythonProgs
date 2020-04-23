class Person:
    def __init__(self,id,name,age): #instance varibales
        self.id=id
        self.name=name
        self.age=age
        

p = Person(1000,"user1",67)
# print obj data
print("************p data************")
print(p.id)
print(p.name)
print(p.age)

p = Person(2000,"user2",69)
# print obj data
print("************p data************")
print(p.id)
print(p.name)
print(p.age)
