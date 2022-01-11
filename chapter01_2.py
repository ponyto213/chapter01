import pandas as pd
import numpy as np

# pandas中有两个数据类型DateFrame和Series
"""
Series：    一种类似于一维数组的对象，是由一组数据(各种NumPy数据类型)以及一组与之相关的数据标签(即索引)组成。
            仅由一组数据也可产生简单的Series对象。注意：Series中的索引值是可以重复的。
DataFrame： 一个表格型的数据结构，包含有一组有序的列，每列可以是不同的值类型(数值、字符串、布尔型等)，
            DataFrame即有行索引也有列索引，可以被看做是由Series组成的字典。

"""
df = pd.read_csv(r"D:\BaiduNetdiskDownload\机器学习和推荐系统"
                 r"\hands-on-data-analysis-master\hands-on-data-analysis-master"
                 r"\第一单元项目集合\train.csv")
print(df.columns)
print(df.Cabin.head())

df1 = pd.read_csv(r"D:\BaiduNetdiskDownload\机器学习和推荐系统"
                  r"\hands-on-data-analysis-master\hands-on-data-analysis-master"
                  r"\第一单元项目集合\test_1.csv", index_col=0)

print(df.head())
print(df1.head())
del df1['a']
print(df1.head())
print("*" * 30)

print(df.drop(['PassengerId', 'Name', 'Age', 'Ticket'], axis=1).head(3))
print(df.head())

print("*" * 30)

print(df[df['Age'] < 10].drop(['PassengerId', 'Name', 'Ticket'], axis=1).head())

print("*" * 30)
midage = df[(df["Age"] > 10) & (df["Age"] < 50)]
print(midage.head())

print("*" * 30)
# https://www.cnblogs.com/keye/p/11229863.html 会把原来的索引当成一列数据保留下来
midage = midage.reset_index(drop=True)
print(midage.head(3))
print(midage.loc[[100], ['Pclass', 'Sex']])

print(print(midage.loc[[100, 105, 108], ['Pclass', 'Name', 'Sex']]))

print(print(midage.iloc[[100, 105, 108], [2, 3, 4]]))


