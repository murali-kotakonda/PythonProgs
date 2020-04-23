import xlwt
from xlwt import Workbook
#This package is for writing data and formatting information to older Excel files (ie: .xls

# You’ll learn how to work with packages such as pandas, openpyxl, xlrd, xlutils and pyexcel.
# Workbook is created
wb = Workbook()

# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Data')

sheet1.write(1, 0, 'data1')
sheet1.write(2, 0, 'data2')
sheet1.write(3, 0, 'data3')
sheet1.write(4, 0, 'data5')
sheet1.write(5, 0, 'CLOCK TOWER')
sheet1.write(0, 0, 'user1')
sheet1.write(0, 1, 'user2')
sheet1.write(0, 2, 'user3')
sheet1.write(0, 3, 'user4')
sheet1.write(0, 4, 'user5')
sheet1.write(0, 5, 'user6')

wb.save('example.xls')



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