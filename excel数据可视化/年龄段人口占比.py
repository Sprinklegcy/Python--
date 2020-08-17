import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
df = pd.read_excel("china.xlsx")

N = 2
fig, ax = plt.subplots(figsize=(12, 8))
year = df.columns.values.tolist()[4:-2:N]
# print(year)
age_0_14 = df.iloc[22].values.tolist()[4:-2:N]
age_15_64 = df.iloc[24].values.tolist()[4:-2:N]
age_65_above = df.iloc[28].values.tolist()[4:-2:N]

ax.bar(year, [100] * len(year), label='Population ages 65 and above (% of total)')
plt.bar(year, np.asarray(age_15_64) + np.asarray(age_0_14), label="Population ages 15-64 (% of total)")
plt.bar(year, age_0_14, label="Population ages 0-14 (% of total)")

plt.title("各年龄段人口所占比例")
# ax.legend(["Population ages 65 and above (% of total)", "Population ages 15-64 (% of total)", "Population ages 0-14 (% of total)"])

ax.legend(loc=3, bbox_to_anchor=(0, 1.05))
plt.show()
