numbers = [1, 3, 4, 2]

# Sorting list of Integers in ascending
numbers.sort() # will not create new list , it will alter the original list
print("ascending")
print(numbers)


print("descending")
numbers.sort(reverse=True)
print(numbers)


print("reverse")
numbers.reverse()
print(numbers)










# Sorting list of Integers in descending
numbers = [1, 3, 4, 2]
#sorted funtion creates a new list after sorting

# Sorting list of Integers in ascend
nums2 = sorted(numbers)
print("original ",numbers)
print("after ascending" , nums2)

nums2 = sorted(numbers, reverse=True)
print("original ",numbers)
print("after descending" , nums2)













