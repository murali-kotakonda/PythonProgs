"""
take bankname(string) as input ,
  if bankname value is "sbi"  o/p => ROI is 10%
  if bankname value is "icici"  o/p => ROI is 11%
  if bankname value is "hdfc"  o/p => ROI is 12%
  if bankname value is "citi"  o/p => ROI is 13%
  other than this o/p => invalid bank


at a time only one condition is satisfied .
solution)
if + elif



"""

bankName = input("enter bankname : ")

if bankName == "sbi":
    print("ROI= 10%")
elif bankName == "icici":
    print("ROI= 11%")
elif bankName == "hdfc":
    print("ROI= 12%")
elif bankName == "citi":
    print("ROI= 13%")
else:
    print("invalid bank")
