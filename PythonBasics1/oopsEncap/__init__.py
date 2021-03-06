"""

Case#1:
-----------------------------------------------------
Class Vehicle:

    //instance variables
    wheel,
    engine
    fuel.

    def  brake():
      <logic to stop car>

    def  acclerate(){
     <logic to speed accelerate>

    def  showFuelReading(){
	 <logic to show fuel reading>




Req#1:To stop vehicle
solution:
call the brake()

brake() -> changing the values for the instance variable wheel + engine



Req#2:speedup vehicle
solution) call accelarate() function.

acclearate() - >changing the values for the instance variable wheel + engine using fuel..



Req#3:see the fuel reading:
solution) call the showFuelReading() function..
shows the current state of the fuel



conclusion:
--------------
-> Hide the instance variables and expose the methods.
-> change the instance variables/read the instance variables using the methods.
[any action on obj perform using the method]
-> one action == one method





changes in class:
  1. make instance variables as private
  2.expose the methods to set data and read data (setters & getters)
  for every instance variables provide setter and getter


How to make instance variables private??


note:
if we write __ before the instance variable ==> then the instance variable will become private
if we write __ before the instance method ==> then the instance method will become private



private:
---------
if the instance variable or funtion is private
then it cannot be accessed outside the class.


How to make instance variable private?
class Person:
	id= None   # public
	__id = None # private

Ex:
class Person:
    id = None
    __name = None

id , __name are instance variable
id -> is public , can be accessed outside the class
__name -> is private , cannot access outside the class


class PersonInfo:

    def __init__(self, pId, pName, pAge):
        self.__id = pId
        self.__name = pName
        self.__age = pAge


        # here __id , __name , __age are instance variables and are private [cannot access outside class]


How to make funtion  private?
class Person:
	#public
  def show(self):
      print("")

   #private
   def __myShow(self):
   		print("")






"""