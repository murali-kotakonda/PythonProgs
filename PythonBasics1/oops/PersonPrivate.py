class Data:
    # instance funtion
    def show(self):
        print("hello inside show")

    # instance funtion
    def show2(self):
        print("hello inside show2")
        self.__myPrivate()

    #private funtion
    def __myPrivate(self):
        print('my private ')


# Syntax for obj creation
p1 = Data()

# calling the function
p1.show()
#p1.__myPrivate()
#p1.myPrivate()

p1.show2()
