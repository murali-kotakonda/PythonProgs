a = [1, 2, 3] 
try:  
    print(a[1]) 
    # Throws error since there are only 3 elements in array 
    print(a[3])  
  
except IndexError: 
    print("An error occurred")

print("bye bye")