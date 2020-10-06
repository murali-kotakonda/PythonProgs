def Display():
    print("hello im in global function")



class Data:
    def show(self):
        print("hello im a instance function")



# how to call global function
Display()

# how to call instance function

#1.create the object
d = Data()

#2.call the method using the object
d.show()