import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
df = pd.read_excel("china.xlsx")
year = df.columns.values.tolist()[4:-2:2]
data = df.iloc[-2].values.tolist()[4:-2:2]
female = np.abs(np.asarray(data) - 45) + 10
male = np.abs(100 - np.asarray(data) - 45) + 10

fig = plt.figure(figsize=(12, 8))

size = len(data)
print(size)
x = np.arange(size)
bar_width = 0.4

plt.title("男女比例")
plt.ylim(0, 20)
plt.ylabel("比\n例", rotation=0)
plt.yticks([0, 15], ["$0\%$", "$50\%$"])
plt.xticks(x, year, rotation=45)
plt.xlabel("年份")
plt.bar(x, female,  width=bar_width, label='女性人口占比')
plt.bar(x + bar_width, male, width=bar_width, label='男性人口占比')

plt.legend()
plt.show()
