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

u = User()
u.id=1234
u.name="kumar"
u.branch = "csc"
u.pan="bncpk"
u.printPerson() # logic from Person
u.printStu() # logic from Student
u.printUser() # logic from User
        
