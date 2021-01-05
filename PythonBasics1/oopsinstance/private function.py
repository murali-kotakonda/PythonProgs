"""
How to write the private function:
---------------------------------------
- a private funtion should be written only inside the class
- a private function cannot be accessed outside the class

if we write "__"  before the funtion name then the funtion will become private.

ex:
class Data:

    def show(self):
      print("show")

    def __hello(self):  # private function
        print("helo")


points:

class: Data
instance funtions: show() and __hello()
public instance funtion : show()
private instance funtion : __hello()


"""



def m1():  # global function
    print("global function called")


class Data:

    def show(self):  # instance function
        print("welcome to instance function....")

    def __hello(self):  # private function
        print("helo")

"""
points:

class: Data
instance funtions: show() and __hello()
public instance funtion : show()
private instance funtion : __hello()






"""
# call global function
m1()

# call instance function
d1 = Data()
d1.show()
# d1.hello() --> will not work
# d1.__hello() --> will not work


d2 = Data()
d2.show()