# assigned in class declaration, are class variables 
from builtins import staticmethod
  
class CSStudent:
    stream = 'cse'                  # Class Variable 
    def __init__(self,name,roll): 
        self.name = name            # Instance Variable 
        self.roll = roll            # Instance Variable
    
    @staticmethod
    def showStream():
        print(CSStudent.stream) 
  
    def test1(self):
        print("test self")



# Objects of CSStudent class 
a = CSStudent('ram', 1) 
b = CSStudent('albert', 2)

a.test1()
print(a.name)    # prints "ram"
print(a.roll)    # prints "1"

print(b.name)    # prints "albert"
print(b.roll)    # prints "2"


#access static variable or method using class name.
print(CSStudent.stream) # prints "cse"
CSStudent.showStream()
CSStudent.stream = 'ECE'
print(CSStudent.stream) # prints "ECE"





# Class variables can be accessed using class 
# name also 
