"""
every for loop can be converted to a whil loop.

for loop: use for loop when we know the number of iterations.
while:use for while when we dont know the number of iterations.

while we need only condition ; init and increment are optional.



# Print Hello for 20 times
print("***************************Print Hello for 20 times****************************************")
i=1 #init
while(i<=20): #condition
    print("Hello")
    i= i+1  #increment



print("***************************Print numbers from 1  for 50 ****************************************")
i=1 #init
while(i<=50): #condition
    print(i)
    i= i+1  #increment


print("***************************Print numbers  starts with 3 till 50 increment by 4 ****************************************")

i=3 #init
while(i<=50): #condition
    print(i)
    i= i+4  #increment


"""


"""
Take size as input and print the numbers from 1 till the input size

size = int(input("enter the size"))
i=1 #init
while(i<=size): #condition
    print(i)
    i= i+1  #increment

"""




"""
Req:
take numbers continuosly
and find sum
if the sum reaches 100
stop the prog and print the final sum



sum=0

while(sum<100):
    num = int(input("enter the number"))
    sum= sum + num

print("sum",sum)
"""


"""
Req:
take numbers continuosly
and find sum
if the sum reaches 100
stop the prog and print the final sum
if the input is a negative number dont perform any sum

solution:
ignore when the input is negative num
use continue

sum=0

while(sum<100):
    num = int(input("enter the number"))
    if(num<0):
        continue # to stop current iteration and go to the next iteration
    sum= sum + num

print("sum",sum)
"""

"""
Req:
take numbers continuosly
and find sum
if the sum reaches 100
stop the prog and print the final sum
if the input is a negative number dont perform any sum
if the input value is 999 , then end the prog and print final sum

solution:
use break statement , exit from loop.

"""

sum=0

while(sum<100):
    num = int(input("enter the number"))
    if(num<0):
        continue # to stop current iteration and go to the next iteration
    if(num==999):
        break
    sum= sum + num

print("sum",sum)
