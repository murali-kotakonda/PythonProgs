from composition.AddressData import Address
from composition.PersonData import Person

id= input("enter id")
name= input("enter name")
age= input("enter age")


hno= input("enter hno")
city= input("enter city")
state= input("enter state")
country= input("enter country")
pin= input("enter pin")



myAddr = Address(hno, city, state, country, pin)


 
p1 =Person(id, name, age, myAddr)

# p1.id = id;
# p1.name = name
# p1.age = age
# p1.addr = myAddr

p1.show()
p1.addr.showAddress()
