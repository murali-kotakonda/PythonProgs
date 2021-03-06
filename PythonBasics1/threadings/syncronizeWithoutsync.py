import threading
import time
"""

Req:
amount = 6000

we need to withdraw 
100
200
300
400

at the same time , after  every withdraw you need to print final balance.

sample o/p:
--------------
withdraw= 100 , final bal =5900
withdraw= 300 , final bal =5600
withdraw= 200 , final bal =5400
withdraw= 400 , final bal =5000 
"""


amount = 6000

class Mythread(threading.Thread):
    def __init__(self, name, withdraw):
        threading.Thread.__init__(self)
        self.name = name
        self.withdraw = withdraw
        
    def run(self):
       global amount
       time.sleep(3)
       amount = amount - self.withdraw
       time.sleep(1)
       print("\n name = {} , withdraw= {} , final bal ={}".format(self.name ,self.withdraw ,amount))

threads = []
threads.append(Mythread("th1", 100))
threads.append(Mythread("th2", 200))
threads.append(Mythread("th3", 300))
threads.append(Mythread("th4", 400))
# add thread to CPu queue

for th in threads:
    th.start()

"""
 

o/p:
----
 Run#1:
 name = th3 , withdraw= 300 , final bal =5000
 name = th1 , withdraw= 100 , final bal =5000
 name = th2 , withdraw= 200 , final bal =5000
 name = th4 , withdraw= 400 , final bal =5000
 
 Run#2:
 name = th1 , withdraw= 100 , final bal =5000
 name = th3 , withdraw= 300 , final bal =5000
 name = th4 , withdraw= 400 , final bal =5000
 name = th2 , withdraw= 200 , final bal =5000
 
 problem:
 every thread is trying to modify the same data at the same time and that leads to data inconsitency.
 
 solution:
 use syncronization
"""