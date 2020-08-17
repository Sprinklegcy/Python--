import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
from matplotlib import cm


plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
df = pd.read_excel("china.xlsx")
# print(list(df))
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
