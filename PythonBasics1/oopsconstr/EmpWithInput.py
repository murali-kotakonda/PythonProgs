from Emppy import Emp


def takeInput():
    name = input("enter name")
    id = input("enter id")
    age = input("enter age")
    empObj = Emp(id, name, age)
    return empObj


def myStart():
    empObj = takeInput()
    empObj1 = takeInput()
    empObj.print()
    empObj1.print()


if __name__ == '__main__':
    myStart()

# types classes ---------> Pojo(used for entity representation)  and Component(logic on the pojo objects)
