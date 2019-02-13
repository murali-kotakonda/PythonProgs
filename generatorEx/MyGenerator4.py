def my_gen(size):
    n = 1
    while(n<=size):
        yield n
        n = n+1

# Using for loop
for item in my_gen(5):
    print(item) 
    
    
for item in my_gen(7):
    print(item) 