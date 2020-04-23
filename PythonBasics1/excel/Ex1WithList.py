import xlwt
from xlwt import Workbook

wb = Workbook()

# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Data')

list = [
    (10,20),
    (30,56)
]

r=0
for row in list:
    c=0
    for data in row:
        sheet1.write(r,c, data)
        c = c+1
    r = r+1

wb.save('example2.xls')


#This package is for writing data and formatting information to older Excel files (ie: .xls

# You’ll learn how to work with packages such as pandas, openpyxl, xlrd, xlutils and pyexcel.
# Workbook is created