from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference

workbook = Workbook()
sheet = workbook.active

# Let's create some sample sales data
rows = [
    ["YEAR", "CSE", "ECE"],
    [2000, 30, 45],
    [2001, 40, 30],
    [2002, 40, 25],
    [2003, 50, 30],
    [2004, 30, 25],
    [2005, 25, 35],
    [2006, 20, 40],
]

for row in rows:
    sheet.append(row)

chart = BarChart()
data = Reference(worksheet=sheet,
                 min_row=1,
                 max_row=8,
                 min_col=2,
                 max_col=3)

chart.add_data(data, titles_from_data=True)
sheet.add_chart(chart, "E2")

workbook.save("chart.xlsx")


"""
1.workbook obj
2.sheet obj
3.select the data for bar chart
4.bar chart obj
5.add data to chart
6.add bar chart to the sheet

"""