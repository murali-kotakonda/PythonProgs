"""
take input for n1,n2
and perform operation for sum, sub mul, div

write sum ,sub, mul ,div functions inside the class

"""

class Calulator:

    def __init__(self,pN1,pN2):
        self.n1 = pN1
        self.n2 = pN2

    def sum(self):
        res = self.n1 + self.n2
        print("sum = ", res )

    def sub(self):
        r = self.n1 - self.n2
        print("sub = ", r)

    def mul(self):
        r = self.n1 * self.n2
        print("mul = ", r)

    def div(self):
        r = self.n1 / self.n2
        print("div = ", r)

#CLASS : Calulator
#instance variables: n1, n2
#local variables : pN1,pN2
# sum , sub , mul , div are the instance functions

print("******** C1 ************ ")
c1 = Calulator(50,20)
c1.sum()
c1.sub()
c1.div()
c1.mul()


print("******** C2 ************ ")
c2 = Calulator(60,3)
c2.sum()
c2.sub()
c2.div()
c2.mul()







