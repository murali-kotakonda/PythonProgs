"""
take bankname as input

if bankname is "sbi" , o/p: 10%
if bankname is "hdfc" , o/p: 11%
if bankname is "icici" , o/p: 12%
if bankname is "citi" , o/p: 13%
for any other bank , o/p: invalid bank

at a time only one condition is satisfied:
use if + elif

"""
bank = input("enter bank name: ")

if bank == "sbi":
    print("10%")
elif bank == "hdfc":
    print("11%")
elif bank == "icici":
    print("12%")
elif bank == "citi":
    print("13%")
else:
    print("invalid bank")

