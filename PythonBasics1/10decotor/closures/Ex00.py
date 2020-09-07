def hello():
    print("welcome to hello function")

fObj = hello
fObj()


#Example2
def add(x,y ):
    print(x+y)

f1 =add

f1(20,30)
f1(30,80)




def change(text):
    return text.upper()

# create obj for change
f1 = change
print(f1)

# call funtion using object
print(f1('Hello'))
print(f1('kumar'))


