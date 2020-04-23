# Python program to sort a list of strings
lst = ['gfg', 'is', 'a', 'portal', 'for', 'geeks']
# Using sort() function
lst.sort()
print(lst)


lst = ['gfg', 'is', 'a', 'portal', 'for', 'geeks']
# Using sort() function
lst.sort(reverse=True)
print(lst)


print("**********************sort based on length ascending*********************************")
list = ['data123', 'is', 'a', 'portal', 'for', 'geeks']
# Using sort() function with key as len
list.sort(key=len)
print(list)

print("**********************sort based on length descending *********************************")
list = ['data123', 'is', 'a', 'portal', 'for', 'geeks']
# Using sort() function with key as len
list.sort(key=len, reverse=True)
print(list)


