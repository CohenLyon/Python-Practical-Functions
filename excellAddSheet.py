import os
import pandas as pd
from openpyxl import load_workbook


# 功能：将多个csv文件合并到一个Excel的不同Sheet中
# 输入：csv文件路径
def excelAddSheet(csvFilePath):
  os.chdir(csvFilePath)
  output_dir = excelFilePath
  excellWriter = pd.ExcelWriter(os.path.join(output_dir, r"Links-NE.xlsx"), engine="openpyxl")
  pd.DataFrame().to_excel(os.path.join(output_dir, r"Links-NE.xlsx"))
  csvFileList = csvFileName(csvFilePath)  # 获取csv文件列表
  for csvFile in csvFileList:
    csv_name = csvFile[-15:]  # 取决于文件名，需要对应修改
    sheet_name = csv_name[:-4]  # 取决于文件后缀，一般不需要修改
    dataframe = pd.read_csv(csv_name)
    book = load_workbook(excelWriter.path)
    excelWriter.book = book
    dataframe.to_excel(excel_writer=excelWriter, sheet_name=sheet_name, index=False, header=["Fiber-ID",..., "Comment"])  # 最后一列添加备注Comment
    excelWriter.close()
    
