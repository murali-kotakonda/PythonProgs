'''
Created on Jul 23, 2018

@author: I335484

Person has id ,name , age , address [street, hno, city , state, country , pin]
Employee has id ,name , age , address [street , hno,  city , state, country , pin] , pan , pfNo , healthInsuranceNumber

-> create obj and set the data and display the data


Relation between Person and Address: Has-A
Relation between Employee and Address: Has-A
Relation between Person and Employee: Is-A
'''


class Address:
    def __init__(self, street, city, pin, state,country):
        self.street = street
        self.city = city
        self.pin = pin
        self.state=state
        self.country = country

    def showAddressInfo(self):
        print(self.street)
        print(self.city)
        print(self.pin)
        print(self.country)
        print(self.state)


class Person:
    def __init__(self,id,name,age,addr=None):
        self.id=id
        self.name=name
        self.age=age
        self.addr = addr

    def showPersonInfo(self):
        print(self.id)
        print(self.name)
        print(self.age)
        print(self.addr)


class Employee(Person):
    def __init__(self, id, name, age, pfNo, pan, addR):
        Person.__init__(self, id, name, age,addR)
        # calling parent constr from child constr
        # reuse the initializn logic for id,name,age
        self.pfNo = pfNo
        self.pan = pan

    def printEmp(self):
        print(self.pan)