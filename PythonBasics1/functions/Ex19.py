"""
How to access global variables inside the function
"""


city = "bangalore"

def change():
    global city
    city ="hyderabad" # is not modifying the global variable; this is creating new local varible


print(city)

change()

print(city)

