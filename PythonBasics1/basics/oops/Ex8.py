
class Person:
    id=None
    age= None
    name=None

    def show(self):
        print("Hello")

#create object
p1 = Person()  # new object is created

# set data
p1.id = 90
p1.name="kumar"
p1.age = 45

#assign the object
p2 = p1   # assign p1 object to p2 , no new object is created. same object is referred by p1 and p2


#dispaly
print("**************display p1*******************")
print(p1.id)
print(p1.name)
print(p1.age)



print("**************display p2*******************")
print(p2.id)
print(p2.name)
print(p2.age)


p2.id=8000
p2.name= "shyam"
p2.age=45

print("************************after changing p2 *******************************************")
print("**************display p1*******************")
print(p1.id)
print(p1.name)
print(p1.age)


print("**************display p2*******************")
print(p2.id)
print(p2.name)
print(p2.age)

"""
Observation: when p2 is changed p1 is also changed , as p1 and p2 are referring to same object


"""