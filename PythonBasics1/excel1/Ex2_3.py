# print("A1 TO C1")
#read by column

from openpyxl import load_workbook
from openpyxl import Workbook


# create workbook obj

workbook = load_workbook('response.xlsx')

#get sheet obj
sheet = workbook.active



# Get all cells from column A
print("Get all cells from column A")

#rows = sheet["A"]
#rows = sheet["B"]
rows = sheet["C"]

print("**********print entire sheet*****************")
for cell in rows:
        print(cell.value , end= " ")




# Get all cells for a range of columns
rows = sheet["A:B"]
for cell in rows:
       print(cell[0].value,cell[1].value)