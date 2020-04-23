x = input("enter the city")
if x == "hyd":
    print("service is providing for{}".format(x))

if x == "bnlr":
    print("service is proving for {}".format(x))
if x == "chenai":
    print("service is providing for {}".format(x))
if x == "mumbai":
    print("service is providing for {}".format(x))
else:
    print("service not providing".format())


x = input("enter the city")
if x == "hyd"  or   x == "bnlr" or   x == "chenai"  or x == "mumbai":
    print("service is providing for {}".format(x))
else:
    print("service not providing".format())

