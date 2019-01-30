class Person:
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age
    
    def showPersonalInfo(self):
        print(self.id)
        print(self.name)
        print(self.age)



class Employee(Person):
    def __init__(self,id,name,age,pfNo,medicalBenefit):
        Person.__init__(self, id, name, age)
        self.pfNo = pfNo
        self.medicalBenefit = medicalBenefit
        
    def showEmpInfo(self):
        print(self.pfNo)
        print(self.medicalBenefit)
        


p = Person(4500,"user1", 45);

e = Employee(5000, "user2", 60, "bang/13445/", "medi assist")

p.showPersonalInfo()

e.showPersonalInfo()
e.showEmpInfo()



        
    