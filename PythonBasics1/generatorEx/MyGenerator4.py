def myRange(size):
    n = 1
    while(n<=size):
        yield n
        n = n+1

# Using for loop
for item in myRange(5):
    print(item) 
    
    
for item in myRange(7):
    print(item) 