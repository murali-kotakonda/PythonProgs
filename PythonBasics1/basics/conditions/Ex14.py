"""
take cityname as input

if cityname is "chennai" or "bangalore" or "hyd" or "mumbai"  o/p:====> service provided
for any other city ====> service not provided

"""

city = input("enter city : ")

if city == "hyd"  or city == "chennai"  or  city == "bangalore"  or city == "mumbai":
    print("service provided")
else:
    print("service not provided")