"""
# nested functions
(function inside a function)
1.outer function
2.inner function

outer function can be called globally
inner function scope is inside the function, cannot be called directly externally.

inner function can access the data from outer function.
"""

def f1():
    print("hello")
    #creating inner function
    def f2():
        print("hello2")

    #callung inner function
    f2()

#call outer function
f1()



#Ex2 : local funtion
def process(num):
    def sqr():  # local funtion ; is accessble to the main funtion
        print(num * num)
    sqr()

process(20)


#Ex3
def increment(num):
    num = num + 10
    def myfun2():
        print(num)
    myfun2()

increment(50)



#Ex4 [inner function accepting an input arg]
def mul(num1):
    def process(num2):
        print(num1 * num2)
    process(2)

mul(10)




#Ex5 local funtion [inner function returning value ]
def process1(num):
    def sqr():  # local funtion ; is accessble to the main funtion
        return(num * num)
    x= sqr()
    print(x)

process1(20)




#Ex6 [inner function accepting an input arg  and  returning value ]
def mul(num1):
    def process(num2):
        return num1 * num2
    res= process(3)
    print(res)

mul(10)
