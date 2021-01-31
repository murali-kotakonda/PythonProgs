"""
Multiple Inheritence:
------------------------------
-> One child having many parent classes
class Person:

class Employee:

class Staff(Employee , Person):   # Staff is child class for Employee and Person


Staff gets inheritence from Person
Staff gets inheritence from Employee

#Staff will inherit props + methods from Employee , Person.


Req:
Person: id,name
Student : branch
User : id,name , branch ,pan

create obj for User , set data and display.

Solution:
-> Create Person class
-> Create Student class
-> Create User class with Person , Student as parent classes

"""

class Person:
    id=None
    name=None

    def printPerson(self):
        print(self.id, self.name)

class Student:

    branch=None
    def printStu(self):    
      print(self.branch)

# User is child for both Person,Student
class User(Person,Student):
     pan = None
     def printUser(self):
        print(self.pan)


# How many i.v. are there in User :  4  [ id , name , branch , pan]
# How many methods are in User: 3  [printPerson()  printStu()  printUser()   ]


#create obj
u = User()

#set data
u.id=1234
u.name="kumar"
u.branch = "csc"
u.pan="bncpk"

#print data
u.printPerson() # logic from Person
u.printStu() # logic from Student
u.printUser() # logic from User

#call u.show() that should print the user info.
        
