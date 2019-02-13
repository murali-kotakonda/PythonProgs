#lambda arguments : expression
#, anonymous function is valid in between the scope while a regular function is valid in the program.
def squareof(x):
   return x*x
p = squareof(5)
print(p)


f = lambda x: x*x
p = f(5)
print(p)



x= lambda a,b: a if a>b else b 
print(x(10,9))


sum = lambda a,b: (a+b)
print (sum(1, 2))



nums = [2,90,10,8,7,8,23,78]
days = filter(lambda num: num if num%2==0 else '', nums)
for d in days:
   print(d)

 
 
x = lambda a : a + 10
print(x(5))


x = lambda a, b, c : a + b + c
print(x(5, 6, 2))












def squareEx(x):
    return x * x

print(squareEx(10))

sq = lambda x : x*x
print(sq(10))
print(sq(90))


bigF = lambda a,b : a if a>b else b
print(bigF(90,10))


   