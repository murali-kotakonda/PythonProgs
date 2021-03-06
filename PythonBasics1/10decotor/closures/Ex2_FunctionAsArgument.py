#Functions can be passed as arguments to other functions:
# Because functions are objects we can pass them as arguments to other functions.
# Functions that can accept other functions as arguments are also called higher-order functions.
# In the example below, we have created a function greet which takes a function as an argument.
# Python program to illustrate functions 
# can be passed as arguments to other functions 


#Ex4 [pass function obj as argument]
def fun1():
    print("In function1")


def fun2():
    print("In function2")


def generic(funObj): #takes function obj as argument
    funObj()

generic(fun1) # call by passing fun1 obj
generic(fun2) # call by passing fun2 obj



#Ex2
def f1(num):
    print("in f1")
    print(num*2);


def sqr(num):
    print("in sqr")
    print(num*num);


#generic method
def process(func,n1):# takes function obj and num as input
    func(n1)


process(f1,3)
process(sqr,10)



#Ex2
def f1(num):
    print("in f1")
    return num*2;


def sqr(num):
    print("in sqr")
    return num*num;


#generic method
def process(func,n1):# takes function obj and num as input
    print("in process")
    z = func(n1)
    return z


print(process(f1,3))
print(process(sqr,10))






#Ex3
def f1(text):  # input is str
    return text.upper()


def f2(text):  # input is str
    return text.lower()


def greet(funcObj):  # input is fun obj
    greeting = funcObj("hello user how are you")
    print(greeting)
"""
pass f1 obj and f2 obj as args to greet function
"""

f1Obj = f1
f2Obj = f2


greet(f1Obj) #call greet funt by passing f1 obj
greet(f2Obj) #call greet funt by passing f2 obj
