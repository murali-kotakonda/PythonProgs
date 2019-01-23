class User:
    def __init__(self,id,fn,ln):
        self.id= id
        self.fn= fn
        self.ln= ln
        
    def showInfo(self):
        print(self.id)
        print(self.fn)
        print(self.ln)
    
    def sum(self,a,b):
        print("sum = ", a+b)
    


def add(a,b):
    print("sum = ", a+b)
    

# call add function
add(10,20)


#call functn inside a clASS
# create obj
myObj = User(1234,"krishna","kumar")
myObj.showInfo()
myObj.sum(10,20)

 