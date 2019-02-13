#input : int , retuntype : funt obj
def f1(num):
    def sqr():
        return num*num;
    return sqr;


fObj = f1(25)

print(fObj())
 