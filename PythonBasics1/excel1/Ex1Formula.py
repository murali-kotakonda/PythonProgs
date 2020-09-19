from openpyxl import Workbook
#The recommended package for reading and writing Excel 2010 files (ie: .xlsx)

"""
Write to excel with formula:
-----------------------
60 100 90 83.33333333	250

"""

workbook = Workbook()
sheet = workbook.active
sheet = workbook.create_sheet("Mysheet")

sheet["A1"] = 60
sheet["B1"] = 100
sheet["C1"] = 90

sheet["D1"] = "=AVERAGE(A1:C1)"
sheet["E1"] = "=SUM(A1:C1)"

workbook.save(filename="response3.xlsx")

