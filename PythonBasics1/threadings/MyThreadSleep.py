
import threading, time

class Mythread(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
         str ="python is a programming language"
         for ch in str:
             time.sleep(0.25)
             print(ch , end=" ")

th1 = Mythread("myThread1")
th1.start()






