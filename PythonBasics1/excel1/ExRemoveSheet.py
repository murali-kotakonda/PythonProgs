from openpyxl import Workbook,load_workbook
workbook = load_workbook('response.xlsx')

print(workbook.get_sheet_names())

sh = workbook.get_sheet_by_name("Mysheet")
workbook.remove(sh)

workbook.save('response.xlsx')