# code :- reused in diff places of ur project
#solution: write code once and reuse any no of times  ==> FUNTIONS
# EX:
#SYNATX : 1. def keyword to write a function 
#         2. after def specify funtion name
#         3. function can take any data type and can return any data type
# use the indentation for the funtion body

# create a funtion with no input and no output
def sayHi():
    print("hi")
    print("hello")


print("welcome to python function")
# call the function
sayHi()
sayHi()


x=30 # global 
# create funtion that take string as input and append "Mr/Mrs"
def greet(str):
    y=40 # local variable
    print("y = ",y)
    print("Mr/Mrs " +str)
    

# call function
greet("kumar")
greet("shyam")





# funtion that takes twoargs int age and string name and prints value
def showDetails(id,name):
    print(" id = ", id, "name = ", name)

showDetails(200, "user1")
showDetails(7000, "user2")



# funtion that takes twoargs int age and string name , and string is optional and prints value
def showAllDetails(id,name='NA'): # name is optional ; name value will be 'NA' 
    print("showAllDetails id = ", id, "name = ", name)

showAllDetails(89999)  #showAllDetails id =  89999 name =  NA
showAllDetails(7000, "user2")


# funtion that takes twoargs int age and string name , and string is optional and prints value
def showAllDetails2(id=0,name='name not available'): # name is optional ; name value will be 'NA' 
    print("showAllDetails id = ", id, "name = ", name)

showAllDetails2(89999)  #showAllDetails id =  89999 name =  NA
showAllDetails2(7000, "user2")
showAllDetails2()  #showAllDetails id =  Id not available name =  name not available



# funtion returns a value
def getData(str):
    return "Name = "+ str

# cal a funtion and capture the retun value
res = getData("user2")
print(res)

res = getData("shyam")
print(res)



# perform sum of two numbers , 
#if n1 or n2 < 0 then return sum as 0
def sum(n1,n2):
    if n1<0 or n2<0:
        return 0
    return n1+n2

r1 = sum(10,20)
print(r1)
r1 = sum(60,20)
print(r1)
r1 = sum(-100,20)
print(r1)
r1 = sum(100,-20)
print(r1)
r1 = sum(-100,-20)
print(r1)

#Find the rank for given studnet Name , sub1 , sub2 , sub3
# take size as input : 3
# user1 70 , 80 90
# user2 100 90 100
# user3 100 80 70

# assignment : n1, n2,n3  find big number ; make use of funtion big(x,y) , 
#retuns big num
#Find the Factorial of a Number


# use funtions
#input : 5 , output = 5+55+555
#input : 6 , output = 6+66+666




