class MyIterator:

    def __init__(self, num):
        self.num = num;
        
    def __iter__(self):
        self.n = 1
        return self    

    def __next__(self):
      if self.n < self.num:
        res  = self.n * self.n
        self.n = self.n +1; 
        return res;
      else: 
          raise StopIteration  

        
myItrObj = MyIterator(10)

itrObj = iter(myItrObj)

for i in itrObj:
    print(i)