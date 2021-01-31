#global or generic exception handling

list = [1, 2, 3]

x= 50
y =1
try:
    print(list[2])
    print(list[1])  # trying to access 8th element but list has 3 elements

    divRes = x / y
    print("result = ", divRes)

    age = int(input("enter age"))
    print("after concerting age= ", age)

except Exception as ex:# ex is the execption obj
    print("exception occured .Please contact admin.",ex)
else:
    print("No exception")
    print("all operations success")

print("end")