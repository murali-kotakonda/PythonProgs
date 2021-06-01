"""
Threading:
------------
-> concurrent programming/ parallel programming.
-> by default single thread is created by python to run prog.
  

  
-> test 1000 test cases  on chrome , firefox , internet explorer.
  solution: threading.
    
Threads:
------------------------
-threading is used for parallel programming.
 [ Parallel programming means Executing multiple programs at the time]

Advantage of thread:
  -response time is improved
   -utilization of resources


 Thread:
  -thread is a single unit created under the process
  -every thread has its own line of execution
  -every thread is independent

when should we use thread?
-----------------------------------
 -when the tasks are independent of each other,
   i.e.the output of one task is not required for the another task
- TEST the application in multiple browsers


-when the thread is created it would not start immediately, because it is decided
	  by the cpu, then it would run

  we cannot determine when the thread would start or end.


  thread states:
 --------------------------
	  1. ready state -- when the developer creates the thread and adds to the cpu job list
	  2. running -- when cpu gives appointment to the thread
	  3. possible 3 states after running state
	  		a. dead state or completed state
	  		b. wait state : we don't know the time
	  		c. sleep state : we will know for how long it is going to know sleep






adv:
----
-> save time , response time/Turn around time is improved.

  


Process: Requires seperate memory.
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

By default python creates the main thread.
using the main thread we need to create the additional threads.



use module "threading"

How to create Thread:
-------------------------
1. Create a Thread Class (ex:MyThread) extending threading.Thread
2. Provide the run() function inside the class.

3.create the Object for MyThread.
4.call the start method using the object.
[start method internally calls the run() function]
  
  

    
"""