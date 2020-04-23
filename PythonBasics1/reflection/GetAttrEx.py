class Employee:
    salary = 25000
    company_name= "geeksforgeeks"

#create obj
employee = Employee()

#set data
setattr(employee, "salary", "5566")
setattr(employee, "company_name", "sap")

#print data
print('The name is:', getattr(employee, "company_name"))
print('The sal is:', getattr(employee, "salary"))
