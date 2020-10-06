"""
take bankname(string) as input ,
  if bankname value is "sbi"  o/p => ROI is 10%
  if bankname value is "icici"  o/p => ROI is 11%
  if bankname value is "hdfc"  o/p => ROI is 12%
  if bankname value is "citi"  o/p => ROI is 13%
  other than this o/p => invalid bank
"""
#approach1

x=input("enter value")

if x=="ICCI":
    print("icci rate of interest 10%")

if x=="hdfc":
    print("hdfc interest rate 13%")
if x=="city":
    print("City bank rate is 12 %")
if x=="sbi":
    print("sbi rate if interest is 12.6 %")



#approach2
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
