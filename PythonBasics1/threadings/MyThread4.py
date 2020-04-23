'''
Created on Aug 16, 2018

@author: I335484


'''

import threading
import time


class Mythread(threading.Thread):

    def __init__(self, name, n1 , n2 , oper):
        threading.Thread.__init__(self)
        self.name = name
        self.n1 = n1;
        self.n2 = n2;
        self.oper = oper
        
    def run(self):
       time.sleep(5)
       if(self.oper == 'add'):
           print("add :{}".format(self.n1 + self.n2))
       if(self.oper == 'mul'):
           print("mul :{}".format( self.n1 * self.n2))
       if(self.oper == 'sub'):
           print("sub :{}".format(self.n1 - self.n2))
       if(self.oper == 'div'):
           print("div :{}".format(self.n1 / self.n2))
       
 
# creating thread 
n1 = 40;
n2 = 20;

myTh1 = Mythread("th1", n1, n2, "add")            
myTh2 = Mythread("th2", n1, n2, "mul")
myTh3 = Mythread("th3", n1, n2, "sub")
myTh4 = Mythread("th4", n1, n2, "div")

# add thread to CPu queue
myTh1.start()
myTh2.start()
myTh3.start()
myTh4.start()
 
# wait till all thread execution compltes
myTh1.join()
myTh2.join()
myTh3.join()
myTh4.join()

print("main thread ended")