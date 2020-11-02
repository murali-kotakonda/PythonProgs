import time
import _thread

import threading


class Mythread(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        print("thraed created", name)

    def run(self):
        print("Thread started running ", self.name)
        
 
# creating thread
myTh1 = Mythread("th1")
myTh2 = Mythread("th2")
myTh3 = Mythread("th3")
myTh4 = Mythread("th4")

# add thread to CPu queue
myTh1.start()
myTh2.start()
myTh3.start()
myTh4.start()

print("bye")

#How many threads are running in this program?
# 5 [main , th1, th2, th3, th4 ]