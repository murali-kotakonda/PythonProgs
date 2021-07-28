"""

Person has id,name, age
Employee has id,name, age , pan , pf
Staff has id,name, age , pan , pf , contractId , contractPeriod.


req:
p=Person()
p.input()  # take input  for id,name, age
p.display() # print the data for id,name, age

e = Employee()
e.input()  # take input  for id,name, age , pan , pf
e.display() # print the data for id,name, age , pan , pf


s= Staff()
s.input()  # take input for id,name, age , pan , pf , contractId , contractPeriod.
s.display() # print the data for s.input()  # take input for id,name, age , pan , pf , contractId , contractPeriod.


"""


class Person:
    def showdata(self):
        self.id = input("enter id ")
        self.name = input("enter name")
        self.age = input("enter age")


    def  printdata(self):
        print(self.id)
        print(self.name)
        print(self.age)

# Employee class as child
class Employee(Person):

    def showdata(self):
        Person.showdata(self)
        self.pfNo = input("enter pfno")
        self.pan = input("enter pan")


    def printdata(self):
        Person.printdata(self)
        print(self.pan)
        print(self.pfNo)


class Staff(Employee):
    def showdata(self):
        Employee.showdata(self)
        self.contactId = input("enter contactId")
        self.contarctPeriod = input("enter contarctPeriod")


    def printdata(self):
        Employee.printdata(self)
        print(self.contactId, self.contarctPeriod)

p=Person()
p.showdata()
p.printdata()

emp = Employee()
emp.showdata()
emp.printdata()

l=Staff()
l.showdata()
l.printdata()