import copy

class Person:
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age


    def showPersonInfo(self):
        print(self.id)
        print(self.name)
        print(self.age)

#set data
p1 = Person(2000,"user1",45)
print("***********print p1****************")
p1.showPersonInfo()


p2= copy.copy(p1)
print("***********print p2****************")
p2.showPersonInfo()


p2.id=2001
p2.name="user2"
p2.age=78
print("***********after chagning p2 p2****************")

print("***********print p1****************")
p1.showPersonInfo()

print("***********print p2****************")
p2.showPersonInfo()









