#function with default args

def myfunction(msg="No data"): #now passing the data for msg is optional
    print("data= ", msg)



myfunction("hi")
myfunction()