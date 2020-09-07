#Functions can be passed as arguments to other functions: Because functions are objects we can pass them as arguments to other functions. Functions that can accept other functions as arguments are also called higher-order functions. In the example below, we have created a function greet which takes a function as an argument.
# Python program to illustrate functions 
# can be passed as arguments to other functions 

def f1(text):  # input is str
    return text.upper()


def f2(text):  # input is str
    return text.lower()


def greet(func):  # input is fun obj
    greeting = func("hello user how are you")
    print(greeting)


f1Obj = f1
f2Obj = f2


greet(f1Obj) #call greet funcyon by passing f1 obj
greet(f2Obj) #call greet funcyon by passing f2 obj

