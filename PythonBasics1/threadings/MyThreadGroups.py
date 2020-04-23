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
           print("add = {} " .format(self.n1 + self.n2))
       if(self.oper == 'mul'):
           print("mul = {} " .format(self.n1 * self.n2))
       if(self.oper == 'sub'):
           print("sub = {} " .format(self.n1 - self.n2))
       if(self.oper == 'div'):
           print("div = {} ".format(self.n1 / self.n2))
       
 
# creating thread 
n1 = 40;
n2 = 20;

threads = []
 
threads.append(Mythread("th1", n1, n2, "add"))
threads.append(Mythread("th2", n1, n2, "mul"))
threads.append(Mythread("th3", n1, n2, "sub"))
threads.append(Mythread("th4", n1, n2, "div"))
# add thread to CPu queue

for th in threads:
    th.start()
    
print("main thread ended")

