


#taking string as input and string as output
def getMsg(inputMsg):
    return "your data = " + inputMsg

# Calling function
myData = getMsg("Mythri Technologies")  # capture the optput form the method getMsg
print(myData)

myData = getMsg(67)  # capture the optput form the method getMsg
print(myData)

myData = getMsg(89.88)  # capture the optput form the method getMsg
print(myData)





#sum of two nums
def sum(x,y):
    return x+y

res1 = sum(1,4)
print(res1)




#sum of three nums
def sum(x,y,z):
    return x+y+z
res1 = sum(1,4,5)
print(res1)
print(sum(56,19,10))





#big of two numbers
def big(x,y):
    if(x>y):
        return x
    else:
        return y

s1 = big(3,5)
print(s1)

s2=big(78,5)
print(s2)

s3 = big(45, big(5,8))
print(s3)










# 5. method taking two integers as  input and  return the sum as output , if numbers ae negative then return -1
def performSum(n1, n2):
    if n1 < 0 or n2 < 0:
        return 0
    return n1 + n2

#big of two & big of three

# Calling functions
sumResult1 = performSum(10, 20)
sumResult2 = performSum(20, 50)
sumResult3 = performSum(-20, -50)
print(sumResult1)
print(sumResult2)
print(sumResult3)


print("*******div*******")
def div(n1,n2): # retun either string or int
    if n2==0:
        return "ERROR denominator cannot be zero"
    r = n1/n2
    return r

print(div(20,10))
print(div(2,0))
print(div(2,2))



#funtn returning multi values
def process(x,y):
    x= x+10
    y= y+10
    return "{} {}".format(x,y).split()

a,b = process(5,6)
print(a,b)


