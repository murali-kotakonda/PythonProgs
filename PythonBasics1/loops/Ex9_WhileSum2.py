"""
while loop
take numbers continuosly
and perform sum

if the sum reaches 100 , stop the prog and print the final sum
if the input is negative number dont perform any sum

continue : go to the next iteration
"""

sum =0

while( sum <100):
     num = int(input("enter number : "))
     if num< 0:
          continue

     sum = sum + num

print("final sum = ", sum)