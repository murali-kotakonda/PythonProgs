"""

Req: capture the personinfo with address and print

Steps:
1.Create person obj with data
2.Create address obj with data
3.keep adress obj inside person obj # relating the objs

"""

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


#set data
p1 = Person(2000,"user1",45)


a1 = Address("marathalli","bangalore","67677","KA","IN")

p1.addr = a1


#display data
print(p1.id)
print(p1.name)
print(p1.age)
print(p1.addr.city)
print(p1.addr.country)
print(p1.addr.pin)
print(p1.addr.state)
print(p1.addr.street)

#approach2
print("***********approach2****************")
p1.showPersonInfo()

p1.addr.showAddressInfo()


#Person with 3 addresses
#Person has address, emp has address, student has address


