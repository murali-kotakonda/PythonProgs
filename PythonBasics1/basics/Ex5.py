"""
#how to intake the inputs from the console
# use input() function
#by default input() funtn considers every value as string

syntax:
x = 90 #[value is provided by dev]  
x = input("enter num")  # value provided from console/command prompt


its is the dev responsibility to convert from string to any other data type:

how to convert from str to int?
use int() function


how to convert from str to float?
use float() function


1.How to take string as input
x= input("enter name")

2.How to take int as input
x = int( input("enter num") )


3.How to take float as input
x = float( input("enter decimal") )


"""

a = input("enter a num")
b = input("enter a float")
c = input("enter a string")

print(type(a),type(b),type(c) )


a = int(input("enter a number"))

b= float(input("enter a float"))

c = input("enter a string")

print("value of a  = ", a, type(a))
print("value of b  = ", b,type(b))
print("value of c  = ", c,type(c))



# input two string , sum  not concactination
num1 = "20.32"
num2 = "21.45"


# convert string, float to float  -->float()
n1 = float(num1)
n2 = float(num2)
print(n1+n2)

# input two string , sum  not concactination
num3 = "20.56"
num4 = 51

# convert string, int to float  -->int()
n1 = float(num3)  # convert string to float
n2 = float(num4)  # convert float to float

print(n1+n2)




# input two string , sum  not concactination
num1 = "20"
num2 = "31"

# convert string, float to int  -->int()
n1 = int(num1)
n2 = int(num2)
print(n1+n2)


# input two string , sum  not concactination
num3 = "20"
num4 = 51.56

# convert string, float to int  -->int()
n1 = int(num3)  # convert string to int
n2 = int(num4)  # convert float to int

print(n1+n2)




