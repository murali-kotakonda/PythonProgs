# var args:: accept any number of inputs:::
def show(*data):
    print(data)

show("krishna")
show(100,"user1")
show(1,2,3,4)
show(1,"krishna", 1313.89, True)
show(1,2,3,4,5,6,7,8,9,10,11,12,13,14,145)


def calculateSum(*inputs):
    sum =0
    for i in inputs:
        sum = sum +i
    print("sum = ",sum)

calculateSum(20,30)
calculateSum(20,30,67,90,98)
calculateSum(20,30,12,34,5,6,78)
calculateSum(20)
calculateSum(20,30,9,1,2,3,4,4,5,6,6,6,6,6,6,6,6,6,56)
calculateSum(20,30,12,3,5,657,8,8,8,88,90)