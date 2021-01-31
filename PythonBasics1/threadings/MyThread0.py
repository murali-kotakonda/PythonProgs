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

# add thread to CPu queue
myTh1.start()

print("bye")
