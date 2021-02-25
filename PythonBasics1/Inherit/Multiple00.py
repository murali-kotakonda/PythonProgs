"""
Req:
Person: id,name
Student : branch
User : id,name , branch ,pan

create obj for User , set data and display.

Solution:
-> Create Person class
-> Create Student class
-> Create User class with Person , Student as parent classes
call show() method that should print every thing
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
     def show(self):
         Person.printPerson(self)
         Student.printStu(self)
         print(self.pan)

#create obj
u = User()

#set data
u.id=1234
u.name="kumar"
u.branch = "csc"
u.pan="bncpk"

#print data
u.show() # prints id,name, branch , pan

#call u.show() that should print the user info.
        
