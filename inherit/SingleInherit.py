class Person:
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age
    
    def showPersonalInfo(self):
        print(self.id)
        print(self.name)
        print(self.age)



class Employee(Person):
    def __init__(self,id,name,age,pfNo,pan):
        Person.__init__(self, id, name, age)
        self.pfNo = pfNo
        self.pan = pan
       
    def printEmp(self):
        print(self.pan)
        print(self.pfNo)
       



p = Person(2000,"user1", 56)
emp = Employee(20001, "albert", 54, "testPf", "testPan")

p.showPersonalInfo()
emp.showPersonalInfo()
emp.printEmp()