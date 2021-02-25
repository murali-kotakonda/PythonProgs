"""
1.create a new sheet

2.write the below data

id    name    age
2000  kumar   35


"""
from openpyxl import Workbook

# create workbook obj
workBook = Workbook()


# create a new sheet
sheet = workBook.create_sheet("my data")

sheet["A1"] = "ID"
sheet["B1"] = "NAME"
sheet["C1"] = "AGE"

sheet["A2"] = "1200"
sheet["B2"] = "KUMAR"
sheet["C2"] = "34"

# save file
workBook.save(filename="response.xlsx")






