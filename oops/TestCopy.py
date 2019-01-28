def changeObj(obj):
    obj.id=3000
    obj.name="user5"
    obj.age=54


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
p.show()

changeObj(p)
p.show()
