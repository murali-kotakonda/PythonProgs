"""
#Write the code to perform search by content , without using in operator

cities = ['bangalore', 'chennai', 'mumbai', 'hyd']
city = input("enter city")
if (city in cities):
    print("service provied")
else:
    print("service not provided")

"""
cities = ['bangalore', 'chennai', 'mumbai', 'hyd']
inputCity = input("enter city: ")

found = False
for city in cities:
    if city == inputCity:
        found= True
        break

if(found):
    print("service provided")
else:
    print("service not provided")


