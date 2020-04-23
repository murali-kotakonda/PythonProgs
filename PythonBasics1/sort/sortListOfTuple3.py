# Python code to sort the tuples using second element  
# of sublist Inplace way to sort using sort() 
def Sort(sub_li): 
  
    # reverse = None (Sorts in Ascending order) 
    # key is set to sort using second element of  
    # sublist lambda has been used 
    
    #While sorting via this method the actual content of the tuple is changed, 
    #and just like the previous method, in-place method of sort is performed.
    sub_li.sort(key = lambda x: x[1]) 
    return sub_li 
  
# Driver Code 
sub_li =[('ram', 10), ('akash', 5), ('raj', 20), ('gaurav', 15)] 
print(Sort(sub_li)) 


list1 =[('ram', 10), ('akash', 5), ('raj', 20), ('gaurav', 15)]
list1.sort(key = lambda x: x[1]) 
print(list1) 


# Python code to sort the tuples using second element  
# of sublist Function to sort using sorted() 

#Sorted() sorts a list and always returns a list with the elements in a sorted manner, 
#without modifying the original sequence. 
#It takes three parameters from which two are optional, 
#here we tried to use all of the three:
def Sort2(sub_li): 
  
    # reverse = None (Sorts in Ascending order) 
    # key is set to sort using second element of  
    # sublist lambda has been used 
    return(sorted(sub_li, key = lambda x: x[1]))     
  
# Driver Code 
sub_li =[['rishav', 10], ['akash', 5], ['ram', 20], ['gaurav', 15]] 
print(Sort2(sub_li)) 