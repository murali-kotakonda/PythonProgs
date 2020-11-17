
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


@f1
def f3():
    print("My f3 functn")

@f1
def f4():
    print("F4 function")


print("*********************************** MAIN ********************************************************")


f3()
print("*******************************************************************************************")
f4()
