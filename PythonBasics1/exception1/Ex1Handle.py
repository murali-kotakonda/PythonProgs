list = [1, 2, 3]
try:
    print(list[2])
    print(list[7])  # trying to access 8th element but list has 3 elements
except IndexError as ex: # executed when there is an exception
    print("list operation failed.")
    print("Invalid access to list")
else:# executed when there is no exception
    print("list operation success")

print("bye")


