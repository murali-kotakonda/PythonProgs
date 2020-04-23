from array import *

# array takes only elements of same data type

#approich1
"""
import array
a = array.array('i', [1,3,5,7,9])
print("array = ",a)
i -> integer
d -> decimal
"""



#approich2
"""
import array as arr
a = arr.array('i', [1,3,5,7,9])
print("array = ",a)

"""



array_num = array('f', [1,3,5,7,9]) # i specifies the type
array_num = array('i', [1,3,5,7,9])
array_num1 = array('i', [1,3,5,7,9]) # i specifies the type

for i in array_num:
    print(i)
print("Access first three items individually")
print(array_num[0])
print(array_num[1])
print(array_num[2])

# negative index is alloweds

#length
print(len(array_num))



# append() -> add new element
array_num.append(90)
# extend () -> add multi elements
array_num.extend([90,1,3,4,6,3,3,21,4])
# insert -> add at position
array_num.insert(5,900)


#remoeving elements
array_num.pop() #removed the last element
array_num.pop(3) # removes elemnent at position
array_num.remove(40) # removes the element 40 from the array

array_num = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
print("Original array: "+str(array_num))
array_num.reverse()
print("Reverse the order of the items:")
print(str(array_num))




#program to append items from a specified list.
num_list = [1, 2, 6, -8]
array_num = array('i', [])
print("Items in the list: " + str(num_list))
print("Append items from the list: ")
array_num.fromlist(num_list)
print("Items in the array: "+str(array_num))




#insert(1, 4)
array_num = array('i', [1, 3, 5, 7, 9])
print("Original array: "+str(array_num))
print("Insert new value 4 before 3:")
array_num.insert(1, 4)
print("New array: "+str(array_num))



array_num = array('i', [1, 3, 5, 7, 9])
print("Original array: "+str(array_num))
print("Remove the third item form the array:")
array_num.pop(2)
print("New array: "+str(array_num))


#array contatenation
array3 = array_num + array_num1 # concatenates same datatypes
print("concat = ",array3)

#slicing
print(array3[0:5])
print(array3[0:-2])
print(d[::-1]) # returns the reverse


