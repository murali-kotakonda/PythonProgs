class Address:
    
    def __init__(self,hno,city,state,country,pin):
        self.hno=hno
        self.city=city
        self.state=state
        self.country=country
        self.pin=pin
        
    def showAddress(self):
        print(self.hno)
        print(self.city)
        print(self.state)
        print(self.country)
        print(self.pin)


           