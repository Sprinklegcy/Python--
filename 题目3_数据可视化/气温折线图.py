import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
df = pd.read_csv("lanzhou.csv", encoding='GBK')

DATE = df['日期'].values.tolist()
MAX = df['最高气温'].values.tolist()
MIN = df['最高气温'].values.tolist()

# print(DATE, MAX, MIN, sep="\n")
YEAR = [i for i in range(2011, 2020)]
MAX_YEAR = [[] for _ in range(2011, 2020)]
MIN_YEAR = [[] for _ in range(2011, 2020)]
high, low = [], []

for i in range(len(DATE)):
    year = int(DATE[i][3])
    mx = int(MAX[i][:-1])
    mn = int(MIN[i][:-1])
    MAX_YEAR[year - 1].append(mx)
    MIN_YEAR[year - 1].append(mn)

for h, l in zip(MAX_YEAR, MIN_YEAR):
    high.append(max(h))
    low.append(min(l))

plt.figure(figsize=(8, 6))
plt.title("气温变化曲线")
plt.ylabel("温\n度\n℃", rotation=0)
plt.xlabel("年份")
plt.xticks(YEAR, YEAR)
plt.plot(YEAR, high, 'r-.o')
plt.plot(YEAR, low, 'g:p')

for x in range(len(YEAR)):
    plt.text(YEAR[x], high[x] + 1, high[x])
    plt.text(YEAR[x], low[x] + 1, low[x])
plt.legend(["最高气温", "最低气温"], loc=3, bbox_to_anchor=(0.8, 1))
plt.show()
