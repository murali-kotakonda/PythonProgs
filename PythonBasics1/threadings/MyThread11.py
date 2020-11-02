'''
Created on Aug 16, 2018

@author: I335484


'''

"""

print nums from 10 to 50

create 4 threads
thread1 print from 10 to 20
thread2 print from 21 to 30
thread3 print from 31 to 40
thread4 print from 41 to 50

for every thread the start and end is different.


"""


import threading
import time
import _thread


class Mythread(threading.Thread):

    def __init__(self, name, begin, end):
        threading.Thread.__init__(self)
        self.name = name
        self.begin = begin
        self.end = end

    def run(self):
        time.sleep(5)
        for i in range(self.begin, self.end + 1):
            print("  {} ".format(i))


# creating thread 
myTh1 = Mythread("th1", 10, 20)
myTh2 = Mythread("th2", 20, 30)
myTh3 = Mythread("th3", 30, 40)
myTh4 = Mythread("th4", 40, 50)


# add thread to CPu queue
myTh1.start()
myTh2.start()
myTh3.start()
myTh4.start()


print("bye")
