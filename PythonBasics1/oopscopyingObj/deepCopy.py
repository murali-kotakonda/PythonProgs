import copy

list1 = [34,98,98787,43,9]
print(list1)

#shallow copy
list2=copy.deepcopy(list1)
print(list2)
list2.append(91)


print(list1)
print(list2)


print(id(list1))
print(id(list2))

#project --> dept --> emp---> address
