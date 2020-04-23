#Ex1 : local funtion
def process(num):
    def sqr():  # local funtion ; is accessble to the main funtion
        print(num * num)
    sqr()

process(20)



#Ex2 : local funtion
def process1(num):
    def sqr():  # local funtion ; is accessble to the main funtion
        return(num * num)
    x= sqr()
    print(x)

process1(20)



#input : int , retuntype : funt obj
def f1():
    print("outer start")
    def sqr():
        print("inner funtion")
    print("outer end")
    return sqr;


# get the funtion obj by calling the funtion
fObj = f1()
# fObj is funton obj for sqr()

fObj()  # call the funtion obj, [call the sqr()]



#input : int , retuntype : funt obj
def f1(num):
    def sqr():
        return num * num;

    return sqr;


# get the funtion obj by calling the funtion
fObj = f1(25)
# fObj is funton obj for sqr()

print(fObj())  # call the funtion obj, [call the sqr()]
