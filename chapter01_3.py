# coding:utf-8
import pandas as pd
import numpy as np

df = pd.read_csv(r"D:\BaiduNetdiskDownload\机器学习和推荐系统"
                 r"\hands-on-data-analysis-master\hands-on-data-analysis-master"
                 r"\第一单元项目集合\train.csv",
                 names=['乘客ID', '是否幸存', '仓位等级', '姓名',
                        '性别', '年龄', '兄弟姐妹个数', '父母子女个数', '船票信息',
                        '票价', '客舱', '登船港口'],
                 index_col=0)

print(df.head(6))
# df.head(6).to_csv(r"C:\Users\Ponyto\Desktop\1.csv", encoding='utf-8_sig')
print(df.columns)

print("******" * 4)

data = pd.DataFrame(np.arange(12).reshape(4, 3),
                    index=['3', '1', '2', '4'],  # 行索引
                    columns=['a', 'c', 'b'])  # 列索引

print(data)
"""
   a   c   b
3  0   1   2
1  3   4   5
2  6   7   8
4  9  10  11
"""
print("******" * 4)
print(data.sort_values(by='c', ascending=False))  # 按照指定列进行排序，默认是升序
print("******" * 4)
print(data.sort_index(ascending=False))  # 按照行倒序排列
print(data.sort_index(ascending=True))  # 按照行升序排列
print("******" * 4)

"""
task 02
"""

# 保存在文件查看
df.sort_values(by=['票价', '年龄'], ascending=False).head(21).to_csv(r"C:\Users\Ponyto\Desktop\2.csv", encoding='utf-8_sig')

"""
task03 矩阵运算 略
"""

"""
task04:船上最大的家族有多少人？
"""

print(max(df['兄弟姐妹个数'] + df['父母子女个数']))  # 取出相应数据直接相加
print("******" * 4)

"""
task05: describe 这个之前用过
"""
print(df.describe().to_csv(r"C:\Users\Ponyto\Desktop\3.csv", encoding='utf-8_sig'))

"""
task06:
"""
print(df['票价'].describe())
print("******" * 4)
print(df['父母子女个数'].describe())
print("******" * 4)
print(df['年龄'].describe())


