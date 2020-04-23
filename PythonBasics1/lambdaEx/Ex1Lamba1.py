#lambda arguments : expression
#, anonymous function is valid in between the 
#scope while a regular function is valid in the program.

def squareof(x):
   return x*x

p = squareof(5)
print(p)

f = lambda x : x*x
print(f(5))
print(f(6))


def mysum(x,y):
    return x+y
print(mysum(10,20))

sum = lambda a,b: (a+b)
print (sum(1, 2))


def mysum(x):
    return x+10

x = lambda a: a + 10
print(x(5))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))


def bigger(x,y):
    if x>y:
        return x
    else: 
        return y
 
print(bigger(20,13))
f1 = lambda x,y : x if x>y else y
print(f1(10,9))
print(f1(50,78))


print("printing   even2")
li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = filter(lambda x: x%2==0, li)
#print("itearor ",evenNumbers)
for e in evenNumbers:
   print(e)



print("printing   even")
nums = [2,90,10,8,7,8,23,78]
days = filter(lambda num: num if num%2==0 else '', nums)
for d in days:
   print(d)

