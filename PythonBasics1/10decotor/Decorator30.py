"""
Authorization in Python frameworks such as Flask and Django
Logging
Measuring execution time
Synchronization

"""

#Ex1
def myDecorator(funObj):
    print("**********myDecorator outer*************")
    def alter():
        print("**********alter inner*************")
        res = funObj()  # res = m1() , res will have 10
        res = res +100  # add 10 + 100
        return res
    return alter


@myDecorator
def m1():
    return 10


print(m1())


#Ex2
def removeSpl(function):
    def process():
        s = str(function())
        return s.replace("$","-")
    return process



def convert(function):
    def toUpper():
        s = function()
        return s.upper()

    return toUpper


@convert
@removeSpl
def getStr():
    return 'hello there $ ,where are $ you $'


print(getStr())



