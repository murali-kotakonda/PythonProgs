def addNums(*nums):
    sum =0
    for i in nums:
        sum= sum+i
    print(sum)
    
def big(n1,n2):
    if n1>n2:
        return n1
    else:
        return n2
    
def test():
    addNums(10,20,30)
    addNums(1,2,3,4,5,6,76,768)
    addNums(6,13,45,5,5)