# print("A1 TO C1")
#read by ROW WISE

from openpyxl import load_workbook
from openpyxl import Workbook


# create workbook obj

workbook = load_workbook('response.xlsx')

#get sheet obj
sheet = workbook.active



 # Get all cells from row 2
print("Read by row number")


# rows = sheet[1] - GET 1ST ROW
rows = sheet[2]  #- GET 2nd row

print("**********print entire sheet*****************")
for cell in rows:
        print(cell.value , end= " ")