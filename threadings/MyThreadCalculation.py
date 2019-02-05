from threading import Thread
import time

class MyThread(Thread):
    
    def __init__(self,name,n1,n2,op):
        Thread.__init__(self)
        self.name=name
        self.a=n1
        self.b=n2
        self.op=op
    
    def run(self):
        time.sleep(3);
        print("current thread ::", self.name)
        if self.op =='add':
            sum= self.a+self.b
            print("sum == ",sum )
        if self.op =='sub':
            res= self.a-self.b
            print("sub == ",res )
        if self.op =='mul':
            res= self.a*self.b
            print("mul == ",res )
        if self.op =='div':
            res= self.a/self.b
            print("div == ",res)

#create thread
n1= int(input("enter n1"))
n2= int(input("enter n2"))

th1 = MyThread("thread1",n1,n2,"add")
th2 = MyThread("thread2",n1,n2,"sub")
th3 = MyThread("thread3",n1,n2,"mul")
th4 = MyThread("thread4",n1,n2,"div")

#start thread
th1.start()
th2.start()
th3.start()
th4.start()


#
th1.join();

th2.join();
th3.join();
th4.join();
print("bye bye")