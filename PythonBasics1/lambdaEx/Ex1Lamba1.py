"""
#lambda arguments : expression
-> is also a functoin without name
-> simplified version for a funtion
-> applicable only when the number of lines is less
-> code simplicity

#, anonymous function is valid and is valid  in the scope
# while a regular function is valid in the program.
"""

def squareof(x):
    return x * x


p = squareof(5)
print(p)

#apprch2 using lamda

"""
i/p: y 
expression : y*y

syntax: 

f = lambda <i/p> : <expression>
"""

mySq = lambda y : y*y

print(mySq(10))
print(mySq(5))
print(mySq(4))

#################################################################################################################
# add function
def add(x, y):
    return x + y

print(add(10, 20))
print(add(5, 4))
print(add(4, 20))
#approch2 using lamda
"""
i/p: x,y
expression : x + y
 
"""

myAdd = lambda x,y : x + y
print(myAdd(10,20))
print(myAdd(5,4))
print(myAdd(4,20))

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

myBig = lambda x,y : x if (x>y) else y
print("Big  = ",myBig(20,30))
print("Big  = ",myBig(50,60))
print("Big  = ",myBig(100,70))


mySmall = lambda x,y : y if (x>y) else x
print("Small  = ",mySmall(20,30))
print("Small  = ",mySmall(50,60))
print("Small  = ",mySmall(100,70))

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
for filter we can use inbuilt function filter()
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

