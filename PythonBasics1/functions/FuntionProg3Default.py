# 3.  defining a function with input  and no output ; and input has a default value if not passed
def printMsg(msg='Mumbai'):  # specify deafult value if the argument is not passed
    print(msg)


# Calling function
printMsg("Bangalore")  # BANGALORE
printMsg()  # Mumbai




def printInfo(id, name="Not Applicable"):
    print("id=", id)
    print("NAME ==", name)


printInfo(1000, "user1")
printInfo(1000)



def f2(name = "no Input",input2=55):
    print("input =", name)
    print("2nd arg=", input2)


f2("user1")  # name = "user1" input2=55
f2("user1", 34)  # name= "user1" , input2= 34
f2()  # name = "no Input",input2=55
f2(65)  # name = 65 ,input2=55
f2(input2=65) #name = "no Input", input2 = 65

f2(12)
f2("user1")
f2(1213.78)
f2(True)  
f2()
f2(1)
f2(1,2)
f2(input2=65)





def f1(id,name,age):
    print(id,name,age)

f1(id=23, age=90, name="kmr")
f1(name="kmr",id=23, age=90 )

