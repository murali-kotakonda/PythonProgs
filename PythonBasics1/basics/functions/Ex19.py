"""
How to access global variables inside the function
"""

city = "Hyd"

def change():
    global city   #functn can acces global bvariable city
    city ="bangaore"

print(city)

change()

print(city)