# assigned in class declaration, are class variables 
from builtins import staticmethod
  
# Class for Computer Science Student 
class CSStudent: 
    stream = 'cse'                  # Class Variable 
    def __init__(self,name,roll): 
        self.name = name            # Instance Variable 
        self.roll = roll            # Instance Variable
    
    @staticmethod
    def test():
        print("test") 
  
    def test1(self):
        print("test self") 
# Objects of CSStudent class 
a = CSStudent('Geek', 1) 
b = CSStudent('Nerd', 2)
a.test1() 
CSStudent.test()
CSStudent.stream = 'ECE' 
print(a.stream)  # prints "cse" 
print(b.stream)  # prints "cse" 
print(a.name)    # prints "Geek" 
print(b.name)    # prints "Nerd" 
print(a.roll)    # prints "1" 
print(b.roll)    # prints "2" 

# Class variables can be accessed using class 
# name also 
print(CSStudent.stream) # prints "cse" 