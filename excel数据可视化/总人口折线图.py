import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
df = pd.read_excel("china.xlsx")
# print(list(df))
year = df.columns.values.tolist()[4:-2:5]
# print(year)
data = df.iloc[-1].values.tolist()[4:-2:5]
data = np.asarray(data) / 1e+8
# print(data)
# fig = plt.figure(facecolor='blue')
plt.title("中国总人口(亿人)")
plt.plot(year, data,  marker='o', c='blue', mec='red', mfc='g')

plt.xlabel("年份/年")
plt.ylabel("人口/亿人")
for a, b in zip(year, data):
    plt.text(a, b, '%0.2f' % b, ha='right', va='bottom', fontsize=8)

plt.grid()
plt.show()