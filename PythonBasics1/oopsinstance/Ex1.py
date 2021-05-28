"""
write a instance function to display the obj data

"""
 
def process():
    print("hello im inside process function")
    
    
    
class Person:

    def m1(self):
        print("hello Im in m1() ")

    def m2(self):
        print("hello Im in m2() ")


#call process() , m1() , m2()
process()

#1.create the object
p = Person()

#2.call the instance function using the object
p.m1()
p.m2()