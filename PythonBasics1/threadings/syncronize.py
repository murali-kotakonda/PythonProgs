import threading
import time

amount = 6000;

threadLock = threading.Lock()

class Mythread(threading.Thread):
    def __init__(self, name, withdraw):
        threading.Thread.__init__(self)
        self.name = name
        self.withdraw = withdraw;
        
    def run(self):
       global amount;
       time.sleep(3)
       threadLock.acquire()
       amount = amount - self.withdraw;
       time.sleep(1)
       print("name = {} , withdraw= {} , final bal ={}".format(self.name ,self.withdraw ,amount))
       threadLock.release()

threads = []
threads.append(Mythread("th1", 100))
threads.append(Mythread("th2", 200))
threads.append(Mythread("th3", 300))
threads.append(Mythread("th4", 400))
# add thread to CPu queue

print(threading.main_thread().name)

for th in threads:
    th.start()
