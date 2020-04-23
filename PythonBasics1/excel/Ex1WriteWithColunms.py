import xlwt
from xlwt import Workbook

# You’ll learn how to work with packages such as pandas, openpyxl, xlrd, xlutils and pyexcel.
# Workbook is created
wb = Workbook()

# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')


# The data
cols = ["A", "B", "C", "D", "E"]
txt = [0,1,2,3,4]

# Loop over the rows and columns and fill in the values
value =1
for num in range(5):
      row = sheet1.row(num)
      for index, col in enumerate(cols):
          row.write(index, value)
          value = value+1

# Save the result
wb.save("test.xls")