#if the instance variable or the instance function  starts with '__' then it is private.
#private cannot be accessed outside the class.

class Data:

    __id= None # instance variable is private
    name=None

    # instance funtion
    def show(self):
        print("hello inside show")

    #private funtion
    def __myPrivate(self):
        print('my private ')

   # instance funtion
    def show2(self):
        print("hello inside show2")
        self.__myPrivate()


# Syntax for obj creation
p1 = Data()

# access the instance variables
p1.name = "kumar"
print(p1.name)

# call the funtion
p1.show()

p1.__id = 344566  # compilation as private cannot be accessed outside class
p1.__process()  # compilation as private cannot be accessed outside class

p1.show2()
