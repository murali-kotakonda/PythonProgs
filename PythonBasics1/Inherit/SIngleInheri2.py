#Person class as parent
#logic inside a constr => to initialize the instace variables

class Person:
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age
    
    def showPersonalInfo(self):
        print(self.id)
        print(self.name)
        print(self.age)


#Employee class as child
class Employee(Person):
    def __init__(self,id,name,age,pfNo,pan):
        Person.__init__(self, id, name, age) 
        # calling parent constr from child constr
        # reuse the initializn logic for id,name,age
        self.pfNo = pfNo
        self.pan = pan
       
    def printEmp(self):
        print(self.pan)
        print(self.pfNo)

# emp class is reusing id,name,age and showPersonalInfo() funtn

#create obj for person
print("print person info")
p = Person(2000,"user1", 56)
p.showPersonalInfo()

#create obj for employee
print("print employee info")
emp = Employee(20001, "albert", 54, "testPf", "testPan")
emp.showPersonalInfo()
emp.printEmp()