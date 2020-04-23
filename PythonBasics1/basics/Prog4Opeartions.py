# + , - * % , /
a = 25
b = 10
c = a * b 
print("sum is ", c)

c = a - b 
print("sub is ", c)

c = a / b 
print("div is ", c)

c = a % b 
print("rem is ", c)

e = a ** b # exponential
print(e)

f = a // b # we will get (floor) results
print(f)


z = f
print(z is f) # identity operator ; both are points to same obj

a = 25
b = 10

e = 10 & 12 #prints8  compares binaries  1010 1100    -->1000 = 8 bits wise comparision
e = 10 | 12 # 1010  1100  -> 1110 prints 14
e = 10 >> 2  # converts 1010 to 10
print(e) # 2
e = 10 << 2   # converts 1010 to 101000
print(e) #40

# Examples of Bitwise operators
a = 10
b = 4

# Print bitwise AND operation
print(a & b)

# Print bitwise OR operation
print(a | b)

# Print bitwise NOT operation
print(~a)

# print bitwise XOR operation
print(a ^ b)

# print bitwise right shift operation
print(a >> 2)

# print bitwise left shift operation
print(a << 2)


