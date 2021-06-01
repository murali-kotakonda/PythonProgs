numbers = [ 3, 4, 2,3,12,25,35,14,5,1,64]

# Sorting list of Integers in ascending
"""
for ascending order use numbers.sort()
for descending order use numbers.sort(reverse=True)
sort() function modifies the same list
"""
print("ascending")
print("Before ", numbers)
numbers.sort()
print("After ", numbers)

print("descending")
print("Before ", numbers)
numbers.sort(reverse=True)
print("After ", numbers)





print("reverse")
numbers.reverse()
print(numbers)









"""
for ascending order use sorted()
for descending order use sorted(reverse=True)
sorted() function will not modifies the same list; it will create the new list
"""
numbers = [ 3, 4, 2,3,12,25,35,14,5,1,64]

print("ascending")
print("Before ", numbers)
newList = sorted(numbers)
print("After ", newList)

print("descending")
print("Before ", numbers)
newList = sorted(numbers,reverse=True)
print("After ", newList)
















