
#input : i/p func obj , return type: f2 obj
"""
outer functn : i/p: function obj ;; return :inner functn obj
inner functn : i/p: NA , o/p: NA
              inner functn calls the functn using the function obj
"""
def f1(func):
    print("f1 is called")
    def f2():
        print("f2 is called")
        func()
    return f2


def f3():
    print("My f3 functn")


def f4():
    print("F4 function")

#call f1 function by passing funtn obj "f3"
# capture funtn obj "f2"

f2Obj = f1(f3)    # call outer funtion f1() by passing f3() object and receive f2() object
f2Obj()  #call the inner funtion f2() and f2() function internally calls f3() function

print("*******************************************************************************************")

#call f1 function by passing funtn obj "f4"
# capture funtn obj "f2"
f2Obj = f1(f4)# call outer funtion f1() by passing f4() object and receive f2() object
f2Obj()  #call the inner funtion f2() and f2() function internally calls f4() function