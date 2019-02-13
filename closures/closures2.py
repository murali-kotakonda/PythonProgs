#Functions are objects: Python functions are first class objects.
#In the example below, we are assigning function to a variable. 
#This assignment doesn’t call the function. 
#It takes the function object referenced by shout and creates a second name pointing to it, yell.
#Python program to illustrate functions can be treated as objects 

num= 1


#closures
def myFun(str):
    num =1;
    def myfun2():
        global num
        num= num+1
        print(str ,num)
    return myfun2;    


fObj = myFun("hello")
fObj()
fObj()



def incrementFun(num):
    def myfun2():
        print(num)
    return myfun2;    


fObj2 = incrementFun(35)
fObj2()
fObj2()



def mul(n1):
    def operate(n2):
        return n1*n2;
    return operate
        
myObj =  mul(2)
print(myObj(6))        
print(myObj(10))

myObj =  mul(3)
print(myObj(6))        
print(myObj(10))


        