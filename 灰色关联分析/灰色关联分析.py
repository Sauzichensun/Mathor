import numpy as np

x_data = np.array([2017,2018,2019,2020,2021,2022])
y_data = np.array([[3806,398,850,1352],
                  [3356,455,846,1268],
                  [2750,482,960,1010],
                  [2335,422,900,953],
                   [2061,561,1024,808],
                   [1988,511,1100,763]])

# 数据预处理
col_means = np.mean(y_data,axis=0) # 求每列的平均值axis=0
y_data = y_data / col_means # np有广播机制不用拓展维度

# 确定分析数列，即因变量与自变量，这里第一列为因变量，其余为自变量

# 确定灰色关联系数,找到两级最小差，与两级最大差
base = y_data[:,0]
y_data[:,1] = np.abs(y_data[:,1] - base)
y_data[:,2] = np.abs(y_data[:,2] - base)
y_data[:,3] = np.abs(y_data[:,3] - base)

a = np.min(y_data[:,1:])
b = np.max(y_data[:,1:])

# 确定ab后，对表中自变量元素定义
p = 0.5 # p可自定义，一般为0.5
y_nay = y_data[:,1:]
y_nay = (a + p*b)/(y_nay + p*b)

# 确定灰色关联度
col_mean = np.mean(y_nay,axis=0)
# 将平均值作为新的一行添加到矩阵末尾
y_nay = np.vstack([y_nay, col_mean])

