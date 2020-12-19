#function with default args

def printInfo(id, name="Not applicable"):# passing id is mandatory and name is optional
    print("ID = ", id)
    print("Name= " , name)
    print("**************************")

#call function
printInfo(2000, "user1")
printInfo(2002)