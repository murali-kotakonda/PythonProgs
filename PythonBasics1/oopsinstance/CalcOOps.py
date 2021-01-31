"""
take input for n1,n2
and perform operation for sum, sub mul div

write sum ,sub, mul ,div functions inside the class

solution:
1.create a class and write 4 instance functions
2.create the object
3.call the 4 instance functions using the obj


#Approach2:
create a Class 'Calc'.
There are two instance variables n1 ,n2 and constructor.
1.take 2 nums as input
2.create object and set the data
3.call functions using the object


"""


class Calculator:

    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def sum(self):
        r = self.n1 + self.n2
        print("sum = ", r)

    def sub(self):
        r = self.n1 - self.n2
        print("sub = ", r)

    def mul(self):
        r = self.n1 * self.n2
        print("mul = ", r)

    def div(self):
        r = self.n1 / self.n2
        print("div = ", r)

    # create obj


c1 = Calculator(30, 20)

# call instance functions
c1.sum()
c1.sub()
c1.mul()
c1.div()


print("*********************************************")
c2 = Calculator(100, 50)

# call instance functions
c2.sum()
c2.sub()
c2.mul()
c2.div()



