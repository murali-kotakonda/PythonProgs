'''
Created on Aug 16, 2018

@author: I335484


'''

import threading
import time
import _thread


class Mythread(threading.Thread):

    def __init__(self, name, n1, n2):
        threading.Thread.__init__(self)
        self.name = name
        self.n1 = n1
        self.n2 = n2

    def run(self):
        for i in range(self.n1, self.n2 + 1):
            print("  {} ".format(i))


# creating thread 
myTh1 = Mythread("th1", 10, 20)
myTh2 = Mythread("th2", 20, 30)
myTh3 = Mythread("th3", 30, 40)
myTh4 = Mythread("th4", 40, 50)


# add thread to CPu queue
print(type(myTh1))
myTh1.start()
myTh2.start()
myTh3.start()
myTh4.start()


print("bye")
