print("****************get file content to list****************")
f3 = open("user.txt", "r")

x= f3.readlines()# returns the list ; list contains entry for every line

print(type(x))

print(x)
f3.close()
