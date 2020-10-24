print("****************get file content to list****************")
f3 = open("user.txt", "r")
x= f3.readlines()
print(type(x))

print(x)
f3.close()


