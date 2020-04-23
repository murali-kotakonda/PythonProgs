def show(*data):
    print(data)


show(1,2,3,4)
show(1,"krishna", 1313.89, True)
show(1,2,3,4,5,6,7,8,9,10,11,12,13,14,145)



def addNums(*nums):
    sum =0
    for i in nums:
        sum = sum +i
    print(sum)

addNums(10,20)
addNums(10,20,30)
addNums(10,20,30,40,50,60)


