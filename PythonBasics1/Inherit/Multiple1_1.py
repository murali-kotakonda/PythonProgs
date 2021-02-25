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


Person constr has 2 args [ id,name ]
Student constr has 1 arg  [ branch ]
User constr has 4 args [id,name , branch ,pan ]
    and call Student constr
        call Person constr
"""
class Person:

    def __init__(self, id, name):
        self.id = id
        self.name =  name

    def printPerson(self):
        print(self.id, self.name)

class Student:

    def __init__(self, branch):
        self.branch = branch        
    
    def printStu(self):    
      print(self.branch)

# User is child for both Person,Student
class User(Person,Student):
     def __init__(self,id,name,branch,pan):
        # call parent constr to init id,name,branch
        Person.__init__(self, id, name)
        Student.__init__(self, branch)
        self.pan = pan

     def show(self):
         Person.printPerson(self)
         Student.printStu(self)
         print(self.pan)

#create obj + set data
u = User(1234,"kumar", "csc", "bncpk")

#print data
u.show()
