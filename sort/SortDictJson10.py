# importing "operator" for implementing itemgetter 
from operator import itemgetter 

#Approach1
# Python code demonstrate the working of 
# sorted() with lambda 
  
# Initializing list of dictionaries 
lis = [{ "name" : "Nandini", "age" : 20},  
{ "name" : "Manjeet", "age" : 20 }, 
{ "name" : "Nikhil" , "age" : 19 }] 
  
# using sorted and lambda to print list sorted 
# by age  
print("The list printed sorting by age: ")
print(sorted(lis, key = lambda i: i['age'])) 
  




#approach2  
# Initializing list of dictionaries 
lis = [{ "name" : "Nandini", "age" : 20},  
{ "name" : "Manjeet", "age" : 20 }, 
{ "name" : "Nikhil" , "age" : 19 }] 
  
# using sorted and itemgetter to print list sorted by age  
print("The list printed sorting by age: ")
print(sorted(lis, key=itemgetter('age'))) 
  
print ("\r") 
  
# using sorted and itemgetter to print list sorted by both age and name 
# notice that "Manjeet" now comes before "Nandini" 
print("The list printed sorting by age and name: ")
print(sorted(lis, key=itemgetter('age', 'name')) )
  
print ("\r") 
  
# using sorted and itemgetter to print list sorted by age in descending order 
print("The list printed sorting by age in descending order: ")
print( sorted(lis, key=itemgetter('age'),reverse = True)) 


# 
# 
# 
# Advantages of itemgetter over lambda
# Performance : itemgetter performs better than lambda functions in the context of time.
# Concise : : itemgetter looks more concise when accessing multiple values than lambda functions.