
# assigned in class declaration, are class variables
from builtins import staticmethod
  
class Student:
    stream = 'cse'                  # Class Variable 
    def __init__(self,name,roll): 
        self.name = name            # Instance Variable 
        self.roll = roll            # Instance Variable
    
    @staticmethod
    def showStream():
        print(CSStudent.stream) 
  
    def show(self):
        print(self.name)
        print(self.roll)



# Objects of CSStudent class 
a = Student('ram', 1)
b = Student('albert', 2)

a.show()
print(a.name)    # prints "ram"
print(a.roll)    # prints "1"

print(b.name)    # prints "albert"
print(b.roll)    # prints "2"


#access static variable or method using class name.
print(Student.stream) # prints "cse"
Student.showStream()
Student.stream = 'ECE'
print(Student.stream) # prints "ECE"





# Class variables can be accessed using class 
# name also 
