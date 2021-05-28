class Person():

    def __init__(self, id , name, age):
        self.id = id
        self.name = name
        self.age = age
        
    def getName(self):
        return self.name
    
    def display(self):
        print("printing from person" , self.id , self.name , self.age)

    def __myprivate(self):
        print("its private")

class Emp(Person):
    
    def __init__(self, id, name, age, projId, deptId):
        '''invoke parent constructor'''        
        Person.__init__(self, id, name, age) 
        self.projId = projId
        self.deptId = deptId
        
    def displayEmp(self):
        print("printing from emp" , 
              self.projId, self.deptId)
      
# Parent class , base class, super class

# child class , sub class , derived class

# thru inheritence props + methods (not private) of parent class are inherited to child clas.


p1 = Person(1000, "user2", 29)
print(p1.getName())
p1.display()

e1 = Emp(1200, "user1", 27, "proj5555", "HR")
print(e1.getName())
e1.display()
e1.displayEmp()  
#e1.myprivate()