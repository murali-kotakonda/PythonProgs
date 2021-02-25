"""
num1  num2   num3   SUM  AVG
10    20     30     60   20


"""
from openpyxl import Workbook

# create workbook obj
workBook = Workbook()


# get the current sheet obj
sheet = workBook.active

sheet["A1"] = "Num1"
sheet["B1"] = "Num2"
sheet["C1"] = "Num3"
sheet["D1"] = "Sum"
sheet["E1"] = "Avg"

sheet["A2"] = 10
sheet["B2"] = 20
sheet["C2"] = 30
sheet["D2"] = "=SUM(A2:C2)"
sheet["E2"] = "=AVERAGE(A2:C2)"

# save file
workBook.save(filename="response.xlsx")






