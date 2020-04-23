#Reflection-enabling functions include type(), isinstance(), callable(), dir() and getattr().

x = 5

def testFunction():
  print("Test")
   
y = testFunction

if (callable(x)):
    print("x is callable")
else:
    print("x is not callable")

if (callable(y)):
    print("y is callable")
else:
    print("y is not callable")
    
y()   


#ex2
class Foo1:
  def __call__(self):
    print('Print Something')

print(callable(Foo1))





#ex3
# Dir : The dir() method tries to return a list of valid attributes of the object. The dir() tries to return a list of valid attributes of the object.
# If the object has __dir__() method, the method will be called and must return the list of attributes.
# If the object doesn’t have __dir()__ method, this method tries to find information from the __dict__ attribute (if defined), and from type object. In this case, the list returned from dir() may not be complete.

number = [1,2,3]
print(dir(number))

characters = ["a", "b"]
print(dir(number))

