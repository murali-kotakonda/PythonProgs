from openpyxl.styles import Font, Color, Alignment, Border, Side, colors
from openpyxl import Workbook

# Create a few styles
bold_font = Font(bold=True)
big_red_text = Font(color=colors.RED, size=20)
center_aligned_text = Alignment(horizontal="center")
double_border_side = Side(border_style="double")
square_border = Border(top=double_border_side,
                        right=double_border_side,
                        bottom=double_border_side,
                        left=double_border_side)

# Style some cells!
workbook = Workbook()
sheet = workbook.active
sheet["A2"].font = bold_font
sheet["A2"] = "nnbsnb"
sheet["A3"].font = big_red_text
sheet["A4"].alignment = center_aligned_text
sheet["A5"].border = square_border
workbook.save(filename="sample_styles.xlsx")



sheet["A6"].alignment = center_aligned_text
sheet["A6"].font = big_red_text
sheet["A6"].border = square_border
workbook.save(filename="testStyles.xlsx")