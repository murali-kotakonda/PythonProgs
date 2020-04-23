# Python3 code to demonstrate  
# removing None values in list 
# using naive method  
  
# initializing list 
test_list = [1, None, 4, None, None, 5, 8, None] 
  
# printing original list  
print ("The original list is : " + str(test_list)) 
  
# using naive method  
# to remove None values in list 
res = [] 
for val in test_list: 
    if val != None : 
        res.append(val) 
  
# printing result 
print ("List after removal of None values : " +  str(res))

#Method #2 : Using list comprehension
#The longer task of using the naive method and increasing line of codes can be done in a compact way using this method. We just check for True values and construct the new filtered list.


# Python3 code to demonstrate  
# removing None values in list 
# using list comprehension 
  
# initializing list 
test_list = [1, None, 4, None, None, 5, 8, None] 
  
# printing original list  
print ("The original list is : " + str(test_list)) 
  
# using list comprehension 
# to remove None values in list 
res = [i for i in test_list if i] 
  
# printing result 
print ("List after removal of None values : " +  str(res))





#Method #3 : Using filter()
#filter function is the most concise and readable way to perform this particular task. It checks for any None value in list and removes them and form a filtered list without the None values.

# Python3 code to demonstrate  
# removing None values in list 
# using filter() 
  
# initializing list 
test_list = [1, None, 4, None, None, 5, 8, None] 
  
# printing original list  
print ("The original list is : " + str(test_list)) 
  
# using filter() 
# to remove None values in list 
res = list(filter(None, test_list)) 
  
# printing result 
print ("List after removal of None values : " +  str(res))   