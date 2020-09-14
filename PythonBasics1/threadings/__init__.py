"""
Threading:
------------
-> concurrent programmimg/ parallel programming.


-> by default single thread is created by python to run prog.
  

  
  
-> test 1000 test cases  on chrome , firefox , internet explorer.
  solution: threading.
    
adv:
----
-> save time , response time/Turn around time is improved.

  
  
module : threading

Process: Requires seprate memory.   
Thread:  
- is a single unit/agent under the process.
- Thread uses the memory allocated for the Process.
- Every thread has its own seprate execution.
- We cannot predict when the thread starts or when the thread ends.
It depends on CPU.
-Every thread has name + priority.
  
  
  
When do we need to create thread?
A) 
  When the tasks  are independent to each other.
  o/p of one task is not required for the other task.
  
         
      

How to create Thread:
-------------------------
1. Create a Thread (ex:MyThread) extending threading.Thread
2. Provide the run() function inside the class.
3.create the Object for MyThread.
4.call the start method using the object.
  
  

    
    
"""