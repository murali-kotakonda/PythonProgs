class RBI:
    def createAccount(self):
        print("RBI:: account created")
        
    def processLoan(self):
        print("RBI:: roi 10%")
    
    def __processPPF(self):
        print("RBI:: roi 10%")

class SBI(RBI):
    def demat1(self):
        print("SBI demat")

class HDFC(RBI):
    def demat2(self):
        print("HDFC demat")

class ICICI(RBI):
    def demat3(self):
        print("ICICI demat")
        
#crate obj
print("**********SBI**********")
sbi = SBI()
sbi.createAccount() # LOGIC FROM RBI
sbi.processLoan() # LOGIC FROM RBI
sbi.demat1() # LOGIC FROM SBI

print("**********HDFC**********")
h = HDFC()
h.createAccount()# LOGIC FROM RBI 
h.processLoan()# LOGIC FROM RBI
h.demat2() # LOGIC FROM HDFC

print("**********ICICI**********")
i = ICICI()
i.createAccount() # LOGIC FROM RBI
i.processLoan() # LOGIC FROM RBI
i.demat3() # LOGIC FROM ICICi