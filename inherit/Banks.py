class RBI:
    def createAccount(self):
        print("RBI:: account created")
        
    def processLoan(self):
        print("RBI:: roi 10%")
    
    def __processPPF(self):
        print("RBI:: roi 10%")

class SBI(RBI):
    def demat(self):
        print("SBI demat")

    def processLoan(self):
        print("SBI:: roi 10%")

class HDFC(RBI):
    def demat(self):
        print("HDFC demat")

class ICICI(RBI):
    def demat(self):
        print("ICICI demat")
        
sbi = SBI()
sbi.createAccount()
sbi.processLoan()
sbi.demat()