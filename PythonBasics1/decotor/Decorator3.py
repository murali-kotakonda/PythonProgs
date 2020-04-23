
#input : func obj , return type: f2 obj
def f1(func):
    print("f1 is called")
    def f2():
        print("f2 is called")
        func()
    return f2


def myFun():
    print("My own functn")


def f3():
    print("F3 function")
#call f1 function by passing funtn obj "myFun"
# capture funtn obj "f2"

f2Obj = f1(myFun) # call outer funtion by passing myFun() object and receive f2() object
f2Obj()  #call the inner funtion f2()

#call f1 function by passing funtn obj "f3"
# capture funtn obj "f2"
f2Obj = f1(f3)
f2Obj()