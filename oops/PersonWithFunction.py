def sum(a,b):
    res = a+b
    print(res)

class Person:
    def __init__(self,id,name,age): #instance varibales
        self.id=id
        self.name=name
        self.age=age
    
    def show(self):
        print(self.id)
        print(self.name)
        print(self.age)
        

p = Person(1000,"user1",67)
p1 = Person(1100,"user8",23)

# print obj data
print("************p data************")
p.show()

# print obj data
print("************p1 data************")
p1.show()

sum(10,20)


