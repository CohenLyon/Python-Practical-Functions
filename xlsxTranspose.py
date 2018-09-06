import xlrd
import wlwt


# 功能：将xlsx文件行列转置
# 输入：（需要装置的xlsx文件）
def xlsxTranspose():
  workbook = xlrd.open_workbook(xlsxFilename)
  write_workbook = xlwt.Workbook(encoding="utf-8")
  worksheet = workbook.sheet()[0]  # 获取第一个sheet
  write_worksheet = write_workbook.add_sheet("Sheet1", cell_overwrite_ok=True)
  for row in range(worksheet.nrows):
    row_content = worksheet.row_values(row)
    for col in range(len(row_content)):
      row_data = worksheet.col_values(col)[row]
      write_worksheet.write(col, row, row_data)
  write_workbook.save(xlsxFilename_transposed)
