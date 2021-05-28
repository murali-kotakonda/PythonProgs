"""
dont take any size as input.

take the numbers continuosly and find the sum.

if the sum reaches 100 then stop the program.
if the input is negative number dont perform any sum
if the input is 999 then stop the prog


solution:
use while loop as we dont know the number of iterations.
use continue statement ->. skip current iteration and it will go to the next iteration
use break statement  -> stops all the iterations and it will come out of the loop
"""
sum = 0

while sum<100:
  num = int(input("enter number: "))

  if(num <0):
    continue

  if (num == 999):
    break

  sum = sum + num

print("sum = ", sum)