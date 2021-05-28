Encapsulation & abstraction:
----------------------------
-> Required for better designing the classes.
->Guidelines & common sense for creating class.


Encapsulation:
->Class is a building block for instance variables & methods
-> We need to create one class per entity
-> Class should contain related instance variables + methods


Case#1:[dont create dupliate classes]
Class Person
  id= None
  name= None
  age= None
  aadhar= None


Class PersonDetails:
  id= None
  name= None
  age= None
  pan= None


Req:
-Create a obj and set data for id,name,age, which class should we use?


solution:
delete any one of the two classes and maintain only one class.
delete PersonDetails class and retain the details  only in person class.

Class Person
  id= None
  name= None
  age= None
  aadhar= None
  pan = None


Case#2: [dont create unrelated instance variables in a class]
-----------
Maintain a vehicle show-room .
capture vehicle & customer info.

class Data:
    vehicleId = None
    vehicelName = None
    vechicleBrand = None
    custId = None
    custName = None
    custMobile= None


If the vehicle comes to show-room then create obj for  Data class
and set values for vehicleId  +  vehicleName  + vechicleBrand

If the customer comes to show-room then create obj for  Data class
and set values for custId  + custName + custMobile


Problems:
  1.This class has unrelated instance variables.
  2. Memory wastage
  3. future enhancement and class becomes complex.

solutions:
  create seperate class for vehicle info
  and create seperate class for customer info


class Vehicle:
    vehicleId = None
    vehicelName = None
    vechicleBrand = None

class Customer:
    custId = None
    custName = None
    custMobile= None


Case#3: [dont create unrelated functions in a class]
---------------------

class Person:
  id =None
  name =None
  age=None

  def sum(self,x,y):
    print("sum = " , (x+y))


req: call sum function
p = Person()
p.sum(20,30)


Problem:
  1.Class has unrelated method
  2.Memory waste

solution:
    -> remove sum() futn from Person class

class Cal:
   def sum(x,y):
      print(x+y)

c = Cal()
c.sum(10,20)







Abstraction:
-> Hide unnecessary data and expose only what ever is required.
->for every action/task there should be only function.






Case#3:
class Person:
  id =None
  name =None
  age=None
  
  def sum(self,x,y):
    print("sum = " , (x+y))
       



req: call sum funtion
  Person p = Person()
  p.sum(10,20)

  
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

class: PersonInfo
constr : __init__
instance variables:  __id , __name , __age
local variables : self, pId, pName, pAge

 # here __id , __name , __age are instance variables and are private [cannot access outside class]


How to make funtion  private?

class Person:

  def show(self):
      print("")


   def __myShow(self):
      print("")


class: Person
instance functions : show() and __myShow()
show():  is a public funtion and can be accessed outside the class
__myShow():  is a private  funtion and cannot be accessed outside the class






"""