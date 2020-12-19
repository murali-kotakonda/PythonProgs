#function with default args

def printInfo(name="Not applicable", age= -1):# passing  name , age is optional
    print("Name= " , name)
    print("age= ", age)
    print("**************************")

#call function
printInfo("user1", 56)
printInfo("Kumar") #name is kumar
printInfo()
