class Address:
    def __init__(self, street, city, pin, state, country):
        self.street = street
        self.city = city
        self.pin = pin
        self.state = state
        self.country = country

    def showAddressInfo(self):
        print(self.street)
        print(self.city)
        print(self.pin)
        print(self.country)
        print(self.state)


class Person:
    def __init__(self, id, name, age, addr=None):
        self.id = id
        self.name = name
        self.age = age
        self.addr = addr

    def showPersonInfo(self):
        print(self.id)
        print(self.name)
        print(self.age)

class Student:
    def __init__(self,name, clgname, semno,branch, addr=None):
        self.d = name
        self.c = clgname
        self.n = semno
        self.b = branch
        self.addr = addr

    def showPersonInfo(self):
        print(self.d)
        print(self.c)
        print(self.n)
        print(self.b)

class Emp:
    def __init__(self,name, cmpname,salary, addr=None):
        self.d = name
        self.c = cmpname
        self.n = salary
        self.addr = addr

    def showPersonInfo(self):
        print(self.d)
        print(self.c)
        print(self.n)

# Create person obj with data
p1 = Person(2000, "user1", 45)
s1=Student("mahe","siddaratha",2,"ece")
e1=Emp("naresh","ims",555)


# Create address obj with data
a1 = Address("marathalli", "bangalore", "67677", "KA", "IN")
a2= Address("t nager", "chennai", "518003", "TN", "IN")
a3  = Address("sr nagaer", "hyderabd", "560037", "TS", "IN")

# keep adress obj inside person obj
p1.addr = a1
s1.addr=a2
e1.addr=a3

print("-------person details-------")
p1.showPersonInfo()
p1.addr.showAddressInfo()

print("=========student details==========")
s1.showPersonInfo()
s1.addr.showAddressInfo()

print("============emp details============")
e1.showPersonInfo()
e1.addr.showAddressInfo()
