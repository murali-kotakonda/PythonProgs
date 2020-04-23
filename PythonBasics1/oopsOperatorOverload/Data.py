class Data:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2

    def __add__(self, other):
        num1= self.n1 + other.n1
        num2 = self.n2 + other.n2
        d = Data(num1,num2)
        return d

    def __sub__(self, other):
        num1 = self.n1 - other.n1
        num2 = self.n2 - other.n2
        d = Data(num1, num2)
        return d

    def __str__(self):
        return "{0} , {1}".format(self.n1,self.n2)

d1= Data(40,20)

d2= Data(5,6)

d3 = d1 + d2 # internally calls __add__
print(d3.n1)
print(d3.n2)


d3 = d1 - d2 # internally calls __sub__
print(d3.n1)
print(d3.n2)



"""


d4 = d1 + d2 + d3
print(d4.n1)
print(d4.n2)
"""

'''     
p1 and p2 are objects.

Operation          how to operate                method to override
addition            p1 + p2                        __add__
Subtraction         p1 - p2                        __sub__
Multiplication      p1 * p2                        __mul__
Power               p1 ** p2                       __pow__(p2)
Division            p1 / p2                        __truediv__(p2)
Floor Division      p1 // p2                       p1.__floordiv__(p2)
Remainder (modulo)  p1 % p2                        p1.__mod__(p2)
Bitwise Left Shift  p1 << p2                       p1.__lshift__(p2)
Bitwise Right Shift p1 >> p2                       p1.__rshift__(p2)
Bitwise AND         p1 & p2                        p1.__and__(p2)
Bitwise OR          p1 | p2                        p1.__or__(p2)
Bitwise XOR         p1 ^ p2                        p1.__xor__(p2)
Bitwise NOT        ~p1                             p1.__invert__() 
'''

'''
Less than                  p1 < p2                        p1.__lt__(p2)
Less than or equal to      p1 <= p2                       p1.__le__(p2)
Equal to                   p1 == p2                       p1.__eq__(p2)
Not equal to               p1 != p2                       p1.__ne__(p2)
Greater than               p1 > p2                        p1.__gt__(p2)
Greater than or equal to   p1 >= p2                       p1.__ge__(p2)
'''
