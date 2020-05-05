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