import xlwt
from xlwt import Workbook

def create_xls(prof_list,filename):
    wb = xlwt.Workbook()
    ws = wb.add_sheet("Sheet 1")
    ws.write(0, 0, "Name")
    ws.write(0, 1, "Job")
    ws.write(0, 2, "University")
    ws.write(0, 3, "Homepage")
    ws.write(0, 4, "H-Index")
    ws.write(0, 5, "Labels")
    ws.write(0,6,"Google Scholar Link")
    iterator=1
    for i in prof_list:
        ws.write(iterator, 0, i.name)
        ws.write(iterator, 1, i.job)
        ws.write(iterator, 2, i.university)
        if(i.homepage==None):
            ws.write(iterator, 3, "N/A")
        else:
            ws.write(iterator, 3, xlwt.Formula('HYPERLINK("%s";"HOMEPAGE")'%i.homepage))
        ws.write(iterator, 4, str(i.h_index))
        ws.write(iterator, 5, str(i.tags))
        ws.write(iterator, 6, xlwt.Formula('HYPERLINK("%s";"GOOGLE SCHOLAR")'%i.gs_link))
        iterator += 1
    wb.save(filename)
    print("[*] Data Saved to Data.xls")

filename = "ex3.xls"

class Data:
    name=None
    job =None
    university = None
    h_index =None
    tags = None
    gs_link=None
    homepage = None

p1 = Data()
p1.name ="user1"
p1.job ="adad"
p1.university ="SVS"
p1.h_index=11
p1.tags ="glglgl"
p1.gs_link ="https://www.gmail.com"
p1.homepage ="https://www.google.com"

prof_list = [ p1]
create_xls(prof_list,filename)