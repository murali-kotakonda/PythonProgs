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

@myDecorator
def m2():
    return 50

print(m1())
print(m2())


#Ex2 [REPLACE $ WITH -)
def removeSpl(function):
    def process():
        s = str(function())
        return s.replace("$","-")
    return process



def convert(function): #CONVERT TO UPPER
    def toUpper():
        s = function()
        return s.upper()

    return toUpper


@convert
@removeSpl
def getStr():
    return 'hello there $ ,where are $ you $'


print(getStr())



