from threading import Thread

class MyThread(Thread):
    def __init__(self,name):
        Thread.__init__(self)
        self.name= name
        print("thread created")

    def run(self):
         print("running thraed", self.name)


#created thraed
th1 = MyThread("th1")
th2 = MyThread("th2")
th3 = MyThread("th3")       

#add cpu job list
th1.start()
th2.start()
th3.start()