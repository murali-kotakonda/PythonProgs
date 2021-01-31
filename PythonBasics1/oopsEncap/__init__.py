"""
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