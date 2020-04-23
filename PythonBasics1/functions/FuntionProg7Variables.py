city ="hyderabd"

def change():
    city="bangalore"


print(city)
change()
print(city)



city ="hyderabd"

def change():
    global city
    city="bangalore"


print(city)
change()
print(city)
