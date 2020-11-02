"""

Req: capture the personinfo with address and print


Steps:
1.Create Address class
2.Create Person class with addObj as instance varibale


3.Create Student obj with data
4.Create address obj with data
5.keep adress obj inside Student obj # relating the objs

"""
from PythonBasics1.oopshasA.Person import Address


class Student:
    def __init__(self,id,firstName,lastName,branch, sem,addr=None):
        self.id = id
        self.firstName=firstName
        self.lastName=lastName
        self.branch=branch
        self.sem = sem

    def showStudent(self):
        print(self.firstName)
        print(self.lastName)
        print(self.branch)
        print(self.sem)

"""
Create Student obj with data
Create address obj with data
keep adress obj inside Student obj # relating the objs
Print Student info and address info
"""


#Create Student obj with data
s1 = Student(2000,"Tom","Johnass","Computer science" , 4)

#Create address obj with data
a1 = Address("thotapalli","hyderabda","345335","tn","IN")

#keep adress obj inside person obj
s1.addr = a1


#display data
print("**********approach1**************")
print(s1.id)
print(s1.firstName)
print(s1.lastName)
print(s1.branch)
print(s1.sem)
print(s1.addr.city)
print(s1.addr.country)
print(s1.addr.pin)
print(s1.addr.state)
print(s1.addr.street)

#approach2
print("***********approach2****************")
s1.showStudent()
s1.addr.showAddressInfo()

#Person with 3 addresses
#Person has address, emp has address, student has address


