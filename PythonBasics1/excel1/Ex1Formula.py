from openpyxl import Workbook
#The recommended package for reading and writing Excel 2010 files (ie: .xlsx)
workbook = Workbook()
sheet = workbook.active
sheet = workbook.create_sheet("Mysheet")

sheet["A1"] = 60
sheet["B1"] = 70
sheet["C1"] = 80

sheet["D1"] = "=AVERAGE(A1:C1)"
sheet["E1"] = "=SUM(A1:C1)"

workbook.save(filename="response1.xlsx")

