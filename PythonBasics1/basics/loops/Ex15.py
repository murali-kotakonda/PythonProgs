"""
dont take any size as input.

take the words continuosly
if the input is 'END' then stop taking words as input
and finally show all the words

solution:
use while loop
"""

word = ""

result = ""

while( word!='END'):
  word = input("enter the word : ")
  result = result + " " + word

print("*****************************************")
print(result)
