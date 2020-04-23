# from <packgename>.<modulename> import <funtion_name>
from assign.Util import big
# big for 2 nums
z  = big(90,19)
print(z)

z  = big(90,119)
print(z)

# big for 3 nums
a=190
b=526
c=176
#z = big(c,big(a,b))
z1  = big(a,b)
z2 = big(c,z1)
print(z2)

# big for any nums
size =int(input("enter size"))
bigNum =0 
for i in range(size):
    n1 = int(input("enter num"))
    bigNum = big(bigNum,n1)

print("big num== ",bigNum)
