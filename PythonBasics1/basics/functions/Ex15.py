"""

function that takes two nums as input and perfoems divisoj;
if num2 is zero then return message"division by zero is not possible"

"""

#WRITE THE FUNCTION
def div(n1,n2):
    if(n2==0):
        return "division by zero is not possible"
    return n1/n2
#div can return int or string

#call the function
print(div(20,2))
print(div(20,0))




