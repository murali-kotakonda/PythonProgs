# same method name in all parent + child class
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
class User(Person,Student):
    def __init__(self,id,name,branch,pan):
        # call parent constr to init id,name,branch
        Person.__init__(self, id, name)
        Student.__init__(self, branch)
        self.pan = pan
    
    def printUser(self):
        print(self.pan)
    
    # overriding
    def save(self):
        print("User :: save")

u = User(1234,"kumar", "csc", "bncpk")
u.printPerson() # logic from Person
u.printStu() # logic from Student
u.printUser() # logic from User
u.save() # logic from User

# when method is called using obj , 1st it wil check in same class
# if not found, then it will look for parent class
