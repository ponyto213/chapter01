import os
'encoding = utf - 8'
import pandas as pd
import numpy as np

df = pd.read_csv(r"D:\BaiduNetdiskDownload\机器学习和推荐系统"
                 r"\hands-on-data-analysis-master\hands-on-data-analysis-master"
                 r"\第一单元项目集合\train.csv",
                 names=['乘客ID', '是否幸存', '仓位等级', '姓名', '性别', '年龄', '兄弟姐妹个数', '父母子女个数', '船票信息', '票价', '客舱', '登船港口'],
                 index_col=0)

# os.getcwd() 查看当前的工作路径

# print(df.head(5))  # 查看前三行

# 1000行进行读取一次
chunksize = pd.read_csv(r"D:\BaiduNetdiskDownload\机器学习和推荐系统"
                        r"\hands-on-data-analysis-master\hands-on-data-analysis-master"
                        r"\第一单元项目集合\train.csv", chunksize=1000)

# 查看数据的基本信息
print(df.info())
print("*" * 20)
print(df.head(10))
print("*" * 20)
print(df.tail(5))
print("*" * 20)

# 判断数据是否为空，为空的地方返回True，其余地方返回False
print(df.isnull().head(6))



df.to_csv(r"D:\BaiduNetdiskDownload\机器学习和推荐系统"
          r"\hands-on-data-analysis-master\hands-on-data-analysis-master"
          r"\第一单元项目集合\train_ch.csv")



