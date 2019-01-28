class Person:
    def __init__(self,id,name,age): #instance varibales
        self.id=id
        self.name=name
        self.age=age
    
    def show(self):
        print(self.id)
        print(self.name)
        print(self.age)
      
p = Person(2000,"user2",78)

p1 = p

p1.id = 3000
p1.name = "user5"
p1.age = 54

print("*******show p data********")
p.show()
print("*******show p1 data********")
p1.show()
