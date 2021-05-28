class Person():

    def __init__(self, id, name):
        self.id = id
        self.name = "person_" + name

    def printPerson(self):
        print(self.id, self.name)    


class Student():

    def __init__(self, branch):
        self.branch = branch        
    
    def printStu(self):    
      print(self.branch)
      
      
class User(Person, Student):
    def __init__(self,id,name,branch,pan):
        Person.__init__(self, id, name)
        Student.__init__(self, branch)
        self.pan = pan
        
    def printUser(self):
        print(self.pan)    


u = User(1234,"murali", "csc", "yaydyayda")
u.printPerson()
u.printStu()
u.printUser()







