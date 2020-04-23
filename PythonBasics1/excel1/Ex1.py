from openpyxl import Workbook
#The recommended package for reading and writing Excel 2010 files (ie: .xlsx)

# create workbook obj
workbook = Workbook()

# sheet obj
sheet = workbook.active
# rename sheet
sheet.title = 'my sheet'

# write data to cells
sheet["A1"] = "id"
sheet["B1"] = "name"
sheet["C1"] = "age"

sheet["A2"] = "90000"
sheet["B2"] = "usr1"
sheet["C2"] = "67"

# save file
workbook.save(filename="response.xlsx")

#sheet = workbook.create_sheet("Mysheet")
#workbook.get_sheet_names()
# workbook.remove_sheet("Mysheet")
