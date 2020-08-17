import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import re

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
df = pd.read_csv("lanzhou.csv", encoding='GBK')

DATE = df['日期'].values.tolist()
weather = df['天气'].values.tolist()

point = [[0 for _ in range(12)] for _ in range(2011, 2020)]

for i in range(len(DATE)):
    if re.search(r'雨|雪', weather[i]):
        point[int(DATE[i][3:4]) - 1][int(DATE[i][5:7]) - 1] += 1

fig, ax = plt.subplots(figsize=(12, 8))

for year in range(9, 0, -1):
    data = np.zeros((12,), dtype=np.int)
    for i in range(0, year):
        data += np.asarray(point[i])
    plt.bar(range(0, 12), data, label="201" + str(year) + "年", width=0.5)

plt.xlabel("月份")
plt.xticks(range(0, 12), range(1, 13))
plt.ylabel("有\n降\n雨\n天\n数\n(天)", rotation=0)
plt.legend()
plt.show()
