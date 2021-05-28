#
"""
create 3 objs , set data and show data
simplify logic for printing the person obj data

solution:
write a function that take obj as the input


"""

def show(pObj):
    print(pObj.id)
    print(pObj.name)
    print(pObj.age)


class person:
    id = None
    name = None
    age = None


# create object
print("************** show p1 *************************")
p1 = person()

p1.id = 1
p1.name = 'raju'
p1.age = 23

show(p1)# then pObj will be p1 , # call funtion by passing p1 object

print("************** show p2 *************************")
p2 = person()

p2.id = 2
p2.name = 'kiran'
p2.age = 25

show(p2)# then pObj will be p2 , # call funtion by passing p2 object

print("************** show p3 *************************")
p3 = person()

p3.id = 3
p3.name = 'ripesh'
p3.age = 26

show(p3)# then pObj will be p3 , # call funtion by passing p3 object

# p1, p2 , p3 are objects
# p1 , p2 ,p3 are global variables
# pObj is a local variable inside show() function

