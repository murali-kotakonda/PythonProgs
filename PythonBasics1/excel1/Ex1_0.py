# write data to excel

from openpyxl import Workbook

# create workbook obj
workbook = Workbook()

#get sheet obj
sheet = workbook.active


# write data to cells


# save file
workbook.save(filename="response.xlsx")