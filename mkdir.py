import os


# 功能：创建新文件夹并打开
# 输入： 新文件夹路径
def mkdir(filePath):
  folder = os.path.exists(filePath)
  if not folder:  # 判断要创建的文件夹是否已存在
    os.makedirs(filePath)
    print("Create the new folder successfully.")
  else:
    print("The folder already exists.")
    
  os.startfile(filePath)  # 打开创建的新文件夹
