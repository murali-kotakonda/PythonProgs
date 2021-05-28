# print("A1 TO C1")

from openpyxl import load_workbook
from openpyxl import Workbook


# create workbook obj

workbook = load_workbook('response.xlsx')

#get sheet obj
sheet = workbook.active

rows = sheet["A1:C1"]

print("**********print entire sheet*****************")
for row in rows:
    print("")
    for cell in row:
        print(cell.value , end= " ")