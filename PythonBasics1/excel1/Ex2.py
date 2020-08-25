from openpyxl import load_workbook
from openpyxl import Workbook

#Example2
workbook = load_workbook(filename="response.xlsx")
print(workbook.sheetnames)
sheet = workbook.active
print(sheet.title)

cell = sheet["A1"]
print(cell.value)


print("rows=",sheet.max_row)
print("rows=",sheet.max_column)
print(sheet.cell(row=1, column=1).value)

print("**********print entire sheet*****************")
for row in sheet.rows:
    print("")
    for c in row:
        print(c.value, end= "  ")



for row in range( 1, sheet.max_row + 1 ):
    for col in range( 0, sheet.max_column ):
        value = sheet[ row ][ col ].value



for row in workbook[ "sheet1" ].rows:
    for cell in row:
        value = cell.value
        print(value)



"""

rows = sheet["A1:C1"]
print("A1 TO C1")
for row in rows:
    for c in row:
        print(c.value)

# Get all cells from column A
cells = sheet["A"]

# Get all cells for a range of columns
cells = sheet["A:B"]

 # Get all cells from row 5
cells = sheet[5]

 # Get all cells for a range of rows
cells = sheet[5:6]

print("rowssssssssssssss")
for row in sheet.iter_rows(min_row=1,
                          max_row=2,
                            min_col=1,
                            max_col=3):
     print(row)

for row in sheet.iter_rows(min_row=1,
                          max_row=2,
                            min_col=1,
                            max_col=3,values_only=True):
 print(row)

"""
