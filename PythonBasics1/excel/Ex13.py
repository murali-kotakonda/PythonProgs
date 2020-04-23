import xlwt
from xlwt import Workbook

def create_xls(filename):
    filename = "ex13.xls"
    wb = xlwt.Workbook()
    ws = wb.add_sheet("Sheet 1")
    ws.write(0, 0, 20)
    ws.write(0, 1, 30)
    ws.write(0, 2, 40)
    ws.write(0, 3, 50)
    ws.write(0, 4, 60)
    ws.write(0, 5, 70)
    ws.write(0,6,80)

    ws.write(0, 7, xlwt.Formula('SUM(A1:G1)'))
    wb.save(filename)
    print("[*] Data Saved to Data.xls")

filename = "ex13.xls"
create_xls(filename)