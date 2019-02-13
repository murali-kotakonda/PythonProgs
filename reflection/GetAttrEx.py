class Employee:
    salary = 25000
    company_name= "geeksforgeeks"

employee = Employee()
print('The salary is:', getattr(employee, "salary"))
print('The salary is:', employee.salary)