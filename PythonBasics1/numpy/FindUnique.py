Method 3 : Using numpy.unique

Using Python’s import numpy, the unique elements in the array are also obtained. In first step convert the list to x=numpy.array(list) and then use numpy.unique(x) function to get the unique values from the list. numpy.unique() returns only the unique values in the list.

filter_none
edit
play_arrow

brightness_4
#Ppython program to check if two  
# to get unique values from list 
# using numpy.unique  
import numpy as np 
  
# function to get unique values 
def unique(list1): 
    x = np.array(list1) 
    print(np.unique(x)) 
      
  
# driver code 
list1 = [10, 20, 10, 30, 40, 40] 
print("the unique values from 1st list is") 
unique(list1) 
  
  
list2 =[1, 2, 1, 1, 3, 4, 3, 3, 5] 
print("\nthe unique values from 2nd list is") 
unique(list2) 