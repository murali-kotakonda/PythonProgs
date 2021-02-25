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


process()

p = Person()
p.m1()
p.m2()

