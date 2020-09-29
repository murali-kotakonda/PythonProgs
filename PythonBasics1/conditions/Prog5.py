"""
take bankname(string) as input ,
  if bankname value is "sbi"  o/p => ROI is 10%
  if bankname value is "icici"  o/p => ROI is 11%
  if bankname value is "hdfc"  o/p => ROI is 12%
  if bankname value is "citi"  o/p => ROI is 13%
  other than this o/p => invalid bank
"""

x=input("enter bank name")
if(x=="hdfc"):
    print("interest rate is 10%")
elif(x=="sbi"):
    print("interest rate is 12%")
elif (x == "icic"):
    print("interest rate is 15%")
elif (x == "yes"):
    print("interest rate is 19%")
else:
    print("bank name is invalid")
