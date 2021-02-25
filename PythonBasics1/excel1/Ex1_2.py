"""
1.create a new sheet

2.write the below data

id    2000
name  kumar
age   35


"""
from openpyxl import Workbook

# create workbook obj
workBook = Workbook()


# create a new sheet
sheet = workBook.create_sheet("my data")

sheet["A1"] = "ID"
sheet["B1"] = "1200"

sheet["A2"] = "NAME"
sheet["B2"] = "KUMAR"

sheet["A3"] = "AGE"
sheet["B3"] = "34"


# save file
workBook.save(filename="response.xlsx")






