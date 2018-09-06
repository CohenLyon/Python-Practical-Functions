import pandas as pd


# 功能：将csv文件转换成xlsx文件
# 输入：csv输入文件路径，xlsx输出文件路径，xlsx输出文件列标数组
def csv_to_xlsx(csvFilename, xlsxFilename, colTitle):
  csv = pd.read_csv(csvFilename, encoding="utf-8")
  colTitle.append("Comment")  # 最后一列添加备注Comment
  csv.to_excel(xlsxFilename, sheet_name="Sheet1", index=False, header=colTitle)
