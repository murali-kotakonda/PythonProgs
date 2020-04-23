# Python program to handle simple runtime error 
#https://www.geeksforgeeks.org/try-except-python/
n1=10
n2=0
try:  
     res= n1/n2
     print("result = ", res)
except ZeroDivisionError: 
    print("An error occurred")
else:
    print("No exception")
finally:
    print("in final")