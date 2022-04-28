

import xlrd

from config.config import *


book = xlrd.open_workbook("../data/case_data.xls")
        # 读取第一个sheet页
table = book.sheet_by_index(0)
print(table.nrows)
# for norw in range(1, table.nrows):
#     if table.cell_value(norw, 4) != "否":  # 每行第4列等于否将不读取内容
#         value = table.row_values(norw)
#         value.pop(4)
#         print(value)


