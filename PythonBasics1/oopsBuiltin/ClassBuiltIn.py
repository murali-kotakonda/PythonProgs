

class Myclass:
    'My documentation'
    
    cName = "sap"
    
    def __init__(self, id, name):
        print("obj created")
        self.id = id
        self.name = name
        
    def __del__(self):
        print('obj deleted')


print(Myclass.__dict__)
print(Myclass.__name__)
print(Myclass.__doc__)
print(Myclass.__module__)
print(Myclass.__bases__)
print(Myclass.cName)

# memory management in python
num = 20  # created obj for 20
num = 45  # new obj with 45 , obj with 20 will garbage collected 


myObj = Myclass(12,"murali")
del myObj
