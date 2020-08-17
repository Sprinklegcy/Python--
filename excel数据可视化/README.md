#### 数据可视化

对excel文件中的数据进行分析和可视化

##### 1.数据的获取

​	从https://datacatalog.worldbank.org/dataset/gender-statistics网站下载数据集，从中找到中国的数据，保存在china.xlsx文件中。

![image-20200624191428407](README.assets/image-20200624191428407.png)

数据包含人口信息，个年龄段人口占比，男女比例，GDP等数据，如下图：

![image-20200624191746893](README.assets/image-20200624191746893.png)

##### 2.可视化展示

​	导入相关库，完成初始化

```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib import cm

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 设置字体，否则中文会显示异常
df = pd.read_excel("china.xlsx")  # 使用pandas读取excel文件
```

###### 	2-1 人口增长折线图

​		使用pandas库读取excel表格中最后一行数据，绘制出折线图，其中N表示步长，可自由指定（下同）。

```python
N = 3
year = df.columns.values.tolist()[4:-2:N]
data = df.iloc[-1].values.tolist()[4:-2:N]  
data = np.asarray(data) / 1e+8
plt.figure(figsize=(12,8))
plt.title("中国总人口(亿人)")
plt.plot(year, data,  marker='o', c='red', mec='blue', mfc='g')

plt.xlabel("年份/年")
plt.ylabel("人口/亿人")
for a, b in zip(year, data):
    plt.text(a, b, '%0.2f' % b, ha='right', va='bottom', fontsize=8)

plt.grid()
plt.show()
```

​	可视化效果：

![image-20200624193427849](README.assets/image-20200624193427849.png)

###### 2-2 男女比例柱状图

​	读取excel文件 “Population, female (% of total)” 对应行数据，用numpy做适当处理，使男女比例展示出来的效果较为明显，绘制出柱状图。

```python
N = 2
year = df.columns.values.tolist()[4:-2:N]
data = df.iloc[-2].values.tolist()[4:-2:N]
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
```

​	可视化效果;

​	![image-20200624193854249](README.assets/image-20200624193854249.png)

###### 2-3 各年龄段人口所占比例堆积柱状图

​	使用pandas库读取"Population ages 65 and above (% of total)", "Population ages 15-64 (% of total)", "Population ages 0-14 (% of total)"三行数据，运用numpy库做相应运算，绘制堆积柱状图。

```python
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
```

可视化效果：

![image-20200624195421990](README.assets/image-20200624195421990.png)

###### 2-4 中国GDP南丁格尔玫瑰图（极坐标图）

​	读取对应行数据，对数据进行开n次方根，目的是缩小数据之间的差距，便于得到更好的展示效果，绘制时使用渐变色进行填充。

```python
N = 2

year = df.columns.values.tolist()[4:-2:N]
# print(year)

rdata = df.iloc[17].values.tolist()[4:-2:N]
data = np.power(np.asarray(rdata), 1 / 7)

theta = np.linspace(0, 2 * np.pi, len(data))  # 等分极坐标系

# 设置画布
fig = plt.figure(figsize=(12, 12),  # 画布尺寸
                 facecolor='lightyellow'  # 画布背景色
                 )

# 设置极坐标系
ax = plt.axes(polar=True)  # 实例化极坐标系
# ax.set_theta_direction(-1)  # 顺时针为极坐标正方向
ax.set_theta_zero_location('N')  # 极坐标 0° 方向为 N

# 设置渐变色
norm = plt.Normalize(data.min(), data.max())
norm_y = norm(data)
map_vir = cm.get_cmap(name='Reds')
color = map_vir(norm_y)


# 在极坐标系中画柱形图
ax.bar(x=theta,  # 柱体的角度坐标
       height=data,  # 柱体的高度, 半径坐标
       width=np.pi * 2 / len(data),  # 柱体的宽度
       # color=np.random.random((len(data), 3))
       color=color
       )

# 绘制中心空白
ax.bar(x=theta,  # 柱体的角度坐标
       height=18,  # 柱体的高度, 半径坐标
       width=0.33,  # 柱体的宽度
       color='white',
       )

ax.bar(x=theta,  # 柱体的角度坐标
       height=21,  # 柱体的高度, 半径坐标
       width=0.33,  # 柱体的宽度
       color='white',
       alpha=0.4
       )

for angle, rd, d, year in zip(theta, rdata, data, year):
    ax.text(angle+0.05, d + 7, "{:.1e} \n".format(rd) + str(year), fontsize=8, rotation=0)  # "%.2e" % data
ax.set_axis_off()
plt.title("GDP (current US$)")
plt.show()
```

可视化效果：

![image-20200624195920505](README.assets/image-20200624195920505.png)