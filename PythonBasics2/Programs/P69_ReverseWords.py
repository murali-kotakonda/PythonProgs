# Author: OMKAR PATHAK

# Python program to reverse the words

userInput = input()
userInput = userInput.split()

print(userInput[::-1])
print(' '.join(userInput[::-1]))

# OUTPUT:
# Computer Science
# Science Computer
