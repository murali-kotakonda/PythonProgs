#Functions can return another function: B
# because functions are objects we can return a function from another function.
#
# In the below example, the create_adder function returns adder function.

# Python program to illustrate functions
# Functions can return another function


"""
Req:
call the inner function globally

solution:
outer function has to return the function
 inner object

"""



#Ex1 input : NA , retuntype : funt obj
def f1():
    print("outer start")
    def sqr():
        print("inner funtion")
    print("outer end")
    return sqr  # return the inner function obj

# get the inner function obj by calling the outer funtion
sqrObj = f1()  # call outer function

# fObj is funton obj for sqr()
sqrObj()  # call inner function sqr()





#Ex2: input : int , retuntype : funt obj
def f1(num):
    def sqr():
        return num * num;
    return sqr;


# get the funtion obj by calling the funtion
sqrObj = f1(25)   # sqrObj is funton obj for sqr()
print(sqrObj())  # call the funtion obj, [call the sqr()]
print(sqrObj())  # call the funtion obj, [call the sqr()]


sqrObj = f1(6)   # sqrObj is funton obj for sqr()
print(sqrObj())  # call the funtion obj, [call the sqr()]


#Ex3 input : int , retuntype : funt obj
def increment(num):
    num = num + 1
    def myfun2():
        print(num)
    return myfun2


innerFobj = increment(35)
innerFobj()
innerFobj()

innerFobj = increment(40)
innerFobj()
innerFobj()


# Ex4: innner functn with arg
#outerfun :i/p: int  , retunr: funvtn obj
#inner funt : i/P -int , retunr :NA
def f1(x):
    print("called f1")

    def f2(y):
        print("called f2")
        print(x + y)

    return f2


f2Obj = f1(15)  # get inner futn obj

f2Obj = f1(25)  # get inner futn obj

f2Obj(10)  # call innner funtn
f2Obj(20)  # call innner funtn
f2Obj(30)  # call innner funtn




#Ex5 inner functn return value

#Outer functn: i/p: int , return : inner functn obj
#Inner functn: i/P : int ,  return : int

def mul(n1):
    def operate(n2):
        return n1 * n2;
    return operate


operateObj = mul(2)
print(operateObj(6)) # multiply 2 * 6
print(operateObj(10)) # multiply 2 * 10

operateObj = mul(3)
print(operateObj(6)) # multiply 3 * 6
print(operateObj(10)) # multiply 3 * 10


