# Import `xlrd`
import xlrd
#xlrd
#This package is for reading data and formatting information from older Excel files (ie: .xls)
# Open a workbook
workbook = xlrd.open_workbook('example.xls')

# Loads only current sheets to memory
#workbook = xlrd.open_workbook('example.xls', on_demand = True)

# Load a specific sheet by name
worksheet = workbook.sheet_by_name('data')

# Load a specific sheet by index
worksheet = workbook.sheet_by_index(0)


print(worksheet.cell(0, 0).value)

print(worksheet.cell_value(0, 0))
print(worksheet.ncols)
print(worksheet.nrows)