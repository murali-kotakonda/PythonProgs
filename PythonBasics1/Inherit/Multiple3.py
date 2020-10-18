#
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

same method name  save() in all parent  classes

"""

"""
when same method is available in both parent class, which method is called?
solution:
use Method Resolution Order. [ depends on the order of declaration. ]
u.save() method logic comes from Person class if  the declaration is : [ class User(Person,Student): ]
u.save() method logic comes from Student class if  the declaration is : [ class User(Student,Person): ]
"""
class Person:

    def __init__(self, id, name):
        self.id = id
        self.name =  name

    def printPerson(self):
        print(self.id, self.name)
        
    def save(self):
        print("Person :: save")

class Student:

    def __init__(self, branch):
        self.branch = branch        
    
    def printStu(self):    
      print(self.branch)
      
    def save(self):
        print("Student :: save")

# User is child for both Person,Student
class User(Person, Student  ):
    def __init__(self,id,name,branch,pan):
        # call parent constr to init id,name,branch
        Person.__init__(self, id, name)
        Student.__init__(self, branch)
        self.pan = pan
    
    def printUser(self):
        print(self.pan)
    

u = User(1234,"murali", "csc", "bncpk")
u.printPerson() # logic from Person
u.printStu() # logic from Student
u.printUser() # logic from User
u.save() # logic from Person

# output depends on the method resolution order
# the order in which the parent classes are declared.

        
