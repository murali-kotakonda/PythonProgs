list = [1, 2, 3]
try:
    print(list[2])
    print(list[7]) #IndexError
except IndexError as ex:
    print("in except block")
    print("invalid access to list.")
else:
    print("no exception ....")
finally:
    print("in finnaly")
    #executed even in case of return statements..
print("bye")


