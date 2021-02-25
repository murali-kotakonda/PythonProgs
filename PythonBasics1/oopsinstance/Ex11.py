"""
write a instance function to display the obj data

- from instance functn we can access the inctance vraibles.
- use self to acces the instacne vraibles
""" 
class Data:
    
    num=None

    def update(self):
        self.num = self.num+10

    def showNum(self):
            print(" num=  ", self.num)


d = Data()
d.num = 20


d.update()
print(d.num)


d.update()
d.update()
d.showNum()


