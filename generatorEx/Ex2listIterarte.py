'''
Created on Aug 20, 2018

@author: I335484
'''

empIds = [100,101,102,103]

#get iterator obj
itr = iter(empIds)


print(next(itr))
print(next(itr))
print(next(itr))
print(itr.__next__())


# iterate using for loop 
for i in itr:
   print(i)
   
# iterate using while   
while True:
  try:  
      num = next(itr)
      print(num)   
  except StopIteration:
      break
