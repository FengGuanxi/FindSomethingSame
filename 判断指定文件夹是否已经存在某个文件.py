# -*- coding:utf-8 -*-
# 判断某个文件是否已经存在在指定文件夹中（即使文件名不同）
import os
import hashlib
import xlwt

def get_md5(file_path):
  md5 = None
  if os.path.isfile(file_path):
    f = open(file_path,'rb')
    md5_obj = hashlib.md5()
    md5_obj.update(f.read())
    hash_code = md5_obj.hexdigest()
    f.close()
    md5 = str(hash_code).lower()  #将字符串中所有大写字母转换成小写字母
  return md5

'''def getFile(filePath,row):
    filesList = os.listdir(filePath)  # 列出文件夹下所有的目录与文件
    print(len(filesList))  # len(imageList)包含了目录数
    for i in range(0, len(filesList)):
        path = os.path.join(filePath, filesList[i])
        print('该文件路径为：', path)
        if os.path.isfile(path):  # 判断是否为文件
            fileMd5 = get_md5(path)
            line = 0
            sheet.write(row, line, path)
            line += 1
            sheet.write(row, line, fileMd5)
            row += 1
        else:
            getFile(path,row)
'''
def getAllFilesMd5(filePath,filesName,md5List):
    filesList=os.listdir(filePath) #列出指定文件夹下的所有目录与文件
    for i in range(0,len(filesList)):
        path=os.path.join(filePath,filesList[i]) #path是一个文件路径字符串
        if os.path.isfile(path): #如果该路径指向的是文件而不是目录
            filesName.append(path)
            fileMd5=get_md5(path)
            md5List.append(fileMd5)
        else: #如果是文件夹则进行递归
            getAllFilesMd5(path,filesName,md5List)

rootDir = r'E:\HDU资料\学习\离散数学\试卷' #我这里是绝对路径，也可以使用相对路径
goalDir = r'C:\Users\FGX\Desktop\test'
#book = xlwt.Workbook(encoding='utf-8', style_compression=0)
#sheet = book.add_sheet('sheet1', cell_overwrite_ok=True)

rootNameList=[];rootMd5List=[]
goalNameList=[];goalMd5List=[]
getAllFilesMd5(rootDir,rootNameList,rootMd5List)
getAllFilesMd5(goalDir,goalNameList,goalMd5List)

print(rootNameList)
for i in range(0,len(goalMd5List)):
    if goalMd5List[i] in rootMd5List:
        num=rootMd5List.index(goalMd5List[i])
        print("文件重复:","源文件夹下文件名为:",rootNameList[num])
        print("目标文件夹下文件名为",goalNameList[i])

#book.save(r'C:\Users\FGX\Desktop/fileMD5.xls')