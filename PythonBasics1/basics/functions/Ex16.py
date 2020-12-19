"""

function that returns multiple values.

"""

#WRITE THE FUNCTION
def process(x,y):
    x= x+10
    y= y+20
    return "{} {}".format(x,y).split()


#call the function
n1, n2 = process(5,6)
print(n1,n2)



