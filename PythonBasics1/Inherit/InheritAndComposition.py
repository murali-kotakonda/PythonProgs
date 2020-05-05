'''
Created on Jul 23, 2018

@author: I335484

Person has id ,name , age , address [street, hno, city , state, country , pin]
Employee has id ,name , age , address [street , hno,  city , state, country , pin] , pan , pfNo , healthInsuranceNumber

-> create obj and set the data and display the data

'''

if __name__ == '__main__':
    pass

class Person(object):

    def __init__(self, id , name, age):
        self.id = id
        self.name = name
        self.age = age
        
    def getName(self):
        return self.name
    
    def display(self):
        print("printing from person" , self.id , self.name , self.age)


class Emp(Person):
    
    def __init__(self, id, name, age, projId, deptId):
        '''invoke parent constructor'''        
        Person.__init__(self, id, name, age)   
        self.projId = projId
        self.deptId = deptId
        
    def display(self):
        Person.display(self)
        print("printing from emp" ,self.projId, self.deptId)


class Staff(Emp):
    
    def __init__(self, id, name, age, projId, deptId, contactId,contarctPeriod):
        '''invoke parent constructor'''        
        Emp.__init__(self, id, name, age,projId,deptId) 
        self.contactId = contactId
        self.contarctPeriod = contarctPeriod
    
    def showStaff(self):
        print("printing from staff",self.contactId, self.contarctPeriod)    



s1 =Staff(1201, "user2", 28, "proj77777", "IT" ,"c_88888","12 months")
print(s1.getName())
s1.display();
s1.showStaff()




