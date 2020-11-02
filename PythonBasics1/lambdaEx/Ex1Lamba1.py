#lambda arguments : expression
#, anonymous function is valid and is valid  in the scope
# while a regular function is valid in the program.


def squareof(x):
    return x * x


p = squareof(5)
print(p)

"""
i/P : x
expression :  x*x

f = lambda <i/p> : <expression>
"""

f = lambda x: x * x
print(f(5))
print(f(6))

#################################################################################################################
def mysum(x,y):
    return x+y

print(mysum(10,20))
"""
i/P : x,y
expresion :  x+y
"""
myFun = lambda  x,y : x + y

print(myFun(20,25))  # 45
print(myFun(25,25))  # 50
print(myFun(30,25))     #55

###############################################################################################################
def mysum(x):
    return x+10

"""
i/P : x
expresion :  x+10
"""
f = lambda x: x+10
print(f(5))
##################################################################################
# lambda for sum of 3 nums
#################################################################################################################
def mysum(a,b,c):
    return a+b+c


sum = lambda a, b, c : a + b + c
print(sum(5, 6, 2))

###################################################################################
def bigger(x,y):
    if x>y:
        return x
    else:
        return y
 
print(bigger(20,13))
print(bigger(3,14))

big = lambda x,y : x if x>y else y
print(big(10,9))
print(big(50,78))

small = lambda x,y : x if x<y else y
print(small(10,9))     # 9
print(small(50,78))    # 50


print("******************** printing   even2 *******************************")
li = [1,2,3,4,5,6,7,8,9,10,-1,20,-45]

# approach1

evenNos = []

for num in li:
    if num % 2 == 0:
        evenNos.append(num)

print(evenNos)


"""
 
  
#approach2
forfilter we cna use inbuilt function filter()
filter() function expects 2 args:
1.list
2.lambda

"""

#Even
isEven = lambda x: x%2==0 #return boolean
list = filter(isEven, li)
for i in list:
    print(i)



#Odd
list = filter(lambda x: x%2!=0 , li)
print(list)


#get positive nums
list = filter(lambda x: x>=0 , li)
print(list)



print("printing   even")
nums = [2,90,10,8,7,8,23,78]
days = filter(lambda num: num if num%2==0 else '', nums)
for d in days:
   print(d)

