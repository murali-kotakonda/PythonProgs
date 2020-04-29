class Person:
    def __init__(self,pId,pName,pAge):
        self.id=pId
        self.name=pName
        self.age=pAge

    def show(self):
            print(self.id)
            print(self.name)
            print(self.age)

#create obj with data
p=Person(2000,"USER1",45) # obj is created , internally calls __init__
p1=Person(2001,"user2",47)  #  obj is created , internally calls __init__

p.show()
p1.show()

p1.name="user5" #change only the name


print(p.id)
print(p.name)
print(p.age)

print(p1.id)
print(p1.name)
print(p1.age)