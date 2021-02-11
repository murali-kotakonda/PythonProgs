"""
while loop
take numbers continuosly
and perform sum

if the sum reaches 100 , stop the prog and print the final sum
"""

sum =0

while( sum <100):
     num = int(input("enter number : "))
     sum = sum + num

print("final sum = ", sum)