"""
dont take any size as input.

take the numbers continuosly and find the sum.

if the sum reaches 100 then stop the program.
if the input is negative number dont perform any sum

solution:
use while loop as we dont know the number of iterations.
use continue statement ;--. skip current iteration and it will go to the next iteration

"""
sum = 0

while(sum<100):
  num = int(input("enter number: "))
  if(num <0):
    continue
  sum = sum + num

print("sum = ", sum)