import numpy

x_data = np.array([[3806, 398, 850, 1352],
                   [3356, 455, 846, 1268],
                   [2750, 482, 960, 1010],
                   [2335, 422, 900, 953],
                   [2061, 561, 1024, 808],
                   [1988, 511, 1100, 763]])

col_means = np.mean(x_data,axis=0) # 求每列的平均值axis=0

x_nomalized = x_data / col_means
