from datetime import datetime
from xlwt import *

font0 = Font()
font0.name = 'Times New Roman'
font0.colour_index = 2
font0.bold = True

style0 = XFStyle()
style0.font = font0
  
wb = Workbook()
ws = wb.add_sheet('A Test Sheet')

ws.write(0, 0, 'My data', style0)

wb.save('example.xls')


"""

style1 = xlwt.XFStyle()
style1.num_format_str = 'D-MMM-YY'


ws.write(0, 0, 'Test', style0)
ws.write(1, 0, datetime.now(), style1)
ws.write(2, 0, 1)
ws.write(2, 1, 1)
ws.write(2, 2, xlwt.Formula("A3+B3"))


"""