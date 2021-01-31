class Person:
    def __init__(self,pId,pName,pAge):
        self.id=pId
        self.name=pName
        self.age=pAge

    def __str__(self):
        return "id ={}, name= {} , age= {}".format(self.id,self.name,self.age)

#create obj with data
p=Person(2000,"USER1",45)


#display
print(p)


"""
By default the print function will print the obj's address.

How to print id,name, age using the same code?
print(p1)

solution:
write __str__ funtion inside the Person class

print(p1) # internally calls the __str__ function

"""

