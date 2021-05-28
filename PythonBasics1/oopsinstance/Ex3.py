"""
class with
- instance variable
- constr
- instance function

write a instance function to display the obj data

- from instance functn we can access the inctance vraibles.
- use self to access the instacne vraibles
"""

class Data:

    def __init__(self, pNum):
        self.num = pNum

    #using instance functn change instance variable
    def update(self):
        self.num = self.num + 100

    # using instance functn print the  instance variable
    def showNum(self):
        print("num = ", self.num)


#call funtions update() and showNum()

d = Data( 400 )

d.showNum()

d.update()

d.showNum()





