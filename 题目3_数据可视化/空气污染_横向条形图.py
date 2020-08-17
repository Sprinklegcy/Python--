import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import re

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
df = pd.read_csv("lanzhou.csv", encoding='GBK')

air = df.loc[2905:, '空气质量'].values.tolist()  # 2019-1-1开始一年的数据
labels = ["优", "良", "轻度污染", "中度污染", "重度污染", "严重污染"]

AQI = [0 for _ in range(6)]

for e in air:
    if e == "优":
        AQI[0] += 1
    elif e == "良":
        AQI[1] += 1
    elif e == "轻度污染":
        AQI[2] += 1
    elif e == "中度污染":
        AQI[3] += 1
    elif e == "重度污染":
        AQI[4] += 1
    elif e == "严重污染":
        AQI[5] += 1

colors = ['#01E400', '#FFFF00', '#FF7E00', '#FE0000', '#98004B', '#7E0123']
plt.figure(figsize=(8, 6))
plt.barh(range(6), AQI[::-1], color=colors[::-1], alpha=0.8, height=0.5)

for i in range(6):
    plt.text(AQI[5 - i], i, str(AQI[5 - i]) + "天")

plt.yticks(range(6), labels[::-1])
plt.xlabel("天数")
plt.show()
