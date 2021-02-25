#self is the current obj under execution

"""
 
#Approach2:
create a Class 'Calc'.
There are two instance variables n1 ,n2 and constructor.
1.take 2 nums as input
2.create object and set the data
3.call functions using the object
 


"""
class Cal:

    n1=None
    n2=None

    def add(self):
        print(self.n1+self.n2)

    def sub(self):
        print(self.n1 - self.n2)

    def mul(self):
        print(self.n1 * self.n2)

    def div(self):
        print(self.n1 / self.n2)

num1 = int(input("enter n1"))
num2 = int(input("enter n2"))

c1 = Cal()
c1.n1 = num1
c1.n2 = num2


c1.add()
c1.sub()
c1.mul()
c1.div()


num1 = int(input("enter n1"))
num2 = int(input("enter n2"))

c2 = Cal()
c2.n1 = num1
c2.n2 = num2

c2.add()
c2.sub()
c2.mul()
c2.div()


