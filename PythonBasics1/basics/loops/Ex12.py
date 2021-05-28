"""
dont take any size as input.

take the numbers continuosly and find the sum.

if the sum reaches 100 then stop the program.

solution:
use while loop as we dont know the number of iterations.


"""
sum = 0

while(sum<100):
  num = int(input("enter number: "))
  sum = sum + num

print("sum = ", sum)