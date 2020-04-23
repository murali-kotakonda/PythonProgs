from openpyxl import load_workbook
from openpyxl import Workbook


workbook = load_workbook(filename="Book1.xlsx")
sheet = workbook.active

print("**********print entire sheet*****************")
for row in sheet.rows:
    print("")
    for c in row:
        print(type(c.value) , c.value, end= "  ")

