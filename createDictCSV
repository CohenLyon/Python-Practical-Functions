import csv


# 功能：将一字典数据写入csv文件
# 输入：列标数组，输出文件地址，字典数据
def createDictCSV(titleKeys, fileName="", dataLinks=[]):
  with open(fileName, "w") as csvFile:
    for key in titleKeys:
      csvFile.write(key)
      csvFile.write(",")
    csvFile.write("\n")
    for link in dataLinks:
      rowData = []
      for key in titleKeys:
        rowData.append(link[key])
       csvFile.write(",".join(rowData))
       csvFile.write("\n")
     csvFile.close()
