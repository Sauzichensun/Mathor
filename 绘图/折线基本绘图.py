import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

x_data = np.array([2017,2018,2019,2020,2021,2022])
y_data = np.array([[3806,398,850,1352],
                  [3356,455,846,1268],
                  [2750,482,960,1010],
                  [2335,422,900,953],
                   [2061,561,1024,808],
                   [1988,511,1100,763]])
# 数据预处理
# x_data[:,0]切片索引
plt.plot(x_data,y_data[:,0],'o-',label='结婚对数',linewidth=2)
plt.plot(x_data,y_data[:,1],'o-',label='房价',linewidth=2)
plt.plot(x_data,y_data[:,2],'o-',label='人均收入',linewidth=2)
plt.plot(x_data,y_data[:,3],'o-',label='女性失业数',linewidth=2)
plt.legend()
plt.title('结婚因素对比')
plt.xlabel('时间')
plt.ylabel('y')
plt.grid(True)
plt.show()
