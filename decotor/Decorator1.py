def f1(num):
    return num*2;


def sqr(num):
    return num*num;


#geeneric method
def process(func,n1):
    return func(n1);


print(process(f1,3))
print(process(sqr,10))
