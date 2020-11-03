#Ex1:
def hello():
    print("welcome to hello function")


# create obj for function
fObj = hello

# call the function
fObj()

#Ex2:
def add(x, y):
    print(x + y)


# create obj for function
f1 = add

# call the function
f1(20, 30)
f1(30, 80)


#Ex3:
def change(text):
    return text.upper()


# create obj for change
f1 = change

# call the function
r1 = f1('Hello')
print(r1)

r2 = f1('kumar')
print(r2)




