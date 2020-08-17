import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import re

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
df = pd.read_csv("lanzhou.csv", encoding='GBK')

weather = df['天气'].values.tolist()

sun = 0  # 晴天
overcast = 0  # 阴天
rain = 0  # 雨
cloudy = 0  # 多云
snow = 0  # 雪

for e in weather:
    if re.search(r'晴', e):
        sun += 1
    if re.search(r'阴', e):
        overcast += 1
    if re.search(r'雨', e):
        rain += 1
    if re.search(r'多云', e):
        cloudy += 1
    if re.search(r'雪', e):
        snow += 1

res = [sun, overcast, rain, cloudy, snow]
count = sum(res)
percent = np.asarray(res) / count

plt.pie(x=percent,
        labels=['晴天', "阴天", "雨", "多云", "雪"],
        autopct='%.1f%%',
        explode=[0.05, 0, 0, 0, 0],
        )  # 设置百分比的格式，这里保留一位小数)

plt.legend(loc='best', bbox_to_anchor=(0.9, 1))
plt.show()
