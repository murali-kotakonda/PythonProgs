# Variables
# ---> local ----> inside funtion ; #local varibles: and can be accessed only inside funtn  scope till functn execution
#----> global--> outside the funtion; this variable is accessible for all functions; till ur prog is avaibale
# local varible memory is allocated when funtn is called
# local varible memory is deallocated when funtn execution compltes

name = "krishna"  # global - create/update varible


def fun1():
    # a function can access the gloabl varible.
    global name
    name = "ram"
    print("printing from func1", name)
    myVar = 123 # local variable , 
    print(myVar)


def fun2():# creates new varible same as global
    name="shyam" #  this is a local variable
    print(name)

    
fun1()
fun2()
print(name)