# constructor :: ------>
#  when obj is created ----> implicitely constr is called....
# purpose ---> intilize the values for properties during obj creation

# obj creation + with ---> 1 single step using contr

num = 20  # global varible


class Emp:
    'Emp class to hold emp details'
    companyName = "sap"  # class variable
    
# structre of constrctr
    def __init__(self, id, name, age):  # instance varibles defined for a constr
        self.id = id
        self.name = name
        self.age = age

    def print(self):
        param = "access"  # local varible
        print(self.id)
        print(self.name)   
        print(self.age)


def execute():
    myObj = Emp(123, "murali", 28)  # created obj with data by invoking contr __init__
    myObj.print()  # explicite call
    myObj1 = Emp(124, "sranya", 29)
    myObj1.print()

    # access static
    print(Emp.companyName) 
    Emp.companyName = "tcs"  # change 
    print(myObj.companyName)
    print(myObj1.companyName)


