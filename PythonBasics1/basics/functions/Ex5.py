"""
write a function for div of two nums.
if num2 is zero print division not possible
"""

#how to write function

def div(x,y):
    if(y==0):
        print(" division not possible")
    else:
        print("divison result = ", x/y)

#how to call the function
div(20,2)
div(5,0)