import json

import pandas as pd

# 读取CSV文件
csvData = pd.read_csv(r'testData.csv', header=0)

# 读取CSV文件包含的列名并转换为list
columns = csvData.columns.tolist()

# 创建空字典
outPut = {}

# 将CSV文件转为字典
for col in columns:
    outPut[col] = str(csvData.loc[0, col])  # 这里一定要将数据类型转成字符串，否则会报错

# 将字典转为json格式
jsonData = json.dumps(outPut)  # 注意此处是dumps，不是dump

# 保存json文件
with open(r'testData.json', 'w') as jsonFile:
    jsonFile.write(jsonData)
