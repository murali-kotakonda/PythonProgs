'''
Created on Aug 16, 2018

@author: I335484

main thread has to end after completing all threads
'''

import threading
import time

class Mythread(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        print("thraed created", name)
        
    def run(self):
        print("running ", self.name , threading.currentThread().getName())
        time.sleep(5)
        print("ended ", self.name)

     
 
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

print("all threads are pipelined..")
#wait till all thread execution compltes
myTh1.join()
myTh2.join()
myTh3.join()
myTh4.join()

print("main thread ended")
print("****************bye*****************")

#assignment:
#main thread to wait for th1 and th1 has to wait for th2


