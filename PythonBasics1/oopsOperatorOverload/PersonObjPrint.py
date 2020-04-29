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
