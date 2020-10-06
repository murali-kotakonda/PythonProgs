class Person:
    def __init__(self,pId,pName,pAge):
        print("constr is called")
        self.id=pId
        self.name=pName
        self.age=pAge

# Person is the class ,
# __init__ is the  constructor

#create obj & set data
p1 = Person(1000,"kumar",43)  # internally calls   __init__
p2 = Person(2000,"raj",33)  # internally calls   __init__

print("***************show p1********************")
#print
print(p1.id)
print(p1.name)
print(p1.age)

print("***************show p2********************")
#print
print(p2.id)
print(p2.name)
print(p2.age)




