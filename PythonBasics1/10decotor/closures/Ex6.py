#Functions are objects:
#Python functions are first class objects.
#In the example below, we are assigning function to a variable.
#This assignment doesnt call the function.
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







