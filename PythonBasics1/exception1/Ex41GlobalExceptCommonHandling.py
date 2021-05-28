"""
Can we write global or generic exception handling?
Yes


syntax:
except Exception as ex:# ex is the execption obj
    <some code>


"""

list = [1, 2, 3]

x = 50
y = 0

age =None


try:
    print(list[0])
    print(list[7])  # trying to access 8th element but list has 4 elements

    divRes = x / y
    print("result = ", divRes)

    age  =  int(input("enter age") )
    print("after concerting age= ",age)
except Exception as ex: #global exception handling
    print("Exception occured due to : ", ex)
else:
    print("No exception")

