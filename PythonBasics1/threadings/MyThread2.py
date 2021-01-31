'''
Created on Aug 16, 2018

@author: I335484


'''

import threading
import time


class Mythread(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print("running " + self.name)
        time.sleep(5)
        print("ended " + self.name)
      
        
 
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

print("****************bye*****************")



#run() method contains the code the thread should execute.


"""
  thread states:
	  1. ready state -- when the developer creates the thread and adds to the cpu job list
	  2. running -- when cpu gives appointment to the thread
	  3. possible 3 states after running state
	  		a. dead state or completed state
	  		b. wait state : we don't know the time
	  		c. sleep state : we will know for how long it is going to know sleep
	  
	       
Thread states:
1.Ready state
myTh1.start()

2.Running state
when run() function is executed

3.sleep  [for a defined time]
time.sleep(5)
AFTER SLEEP it goes back to running state

4.wait state [for a undefined time]
AFTER wait it goes back to running state

5.dead
once the run() method execution is completed.
  
  
"""