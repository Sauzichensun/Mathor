import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import PchipInterpolator, CubicSpline
from scipy.integrate import quad
from scipy.optimize import minimize_scalar

# 定义数据点
# x = np.array([0, 3, 5, 7, 9, 11, 12, 13, 14, 15])
# y = np.array([0, 1.2, 1.7, 2.0, 2.1, 2.0, 1.8, 1.2, 1.0, 1.6])

x = np.array([0.15,0.16,0.17,0.18])
y = np.array([3.5,1.5,2.5,2.8])
# 创建三次埃米特插值对象
hermite_interpolator = PchipInterpolator(x, y)

# 创建三次样条插值对象
spline_interpolator = CubicSpline(x, y, bc_type='natural')

# 定义插值点
x_new = np.linspace(0, 0.2, 10000)
y_hermite = hermite_interpolator(x_new)
y_spline = spline_interpolator(x_new)

# 输出三次埃米特插值的分段多项式函数
print("Cubic Hermite Interpolation piecewise polynomials:")
for i in range(len(x) - 1):
    coeffs = hermite_interpolator.c[:, i]
    print(f"Interval [{x[i]}, {x[i+1]}]:")
    print(f"  {coeffs[0]:.3f}*(t-{x[i]})^3 + {coeffs[1]:.3f}*(t-{x[i]})^2 + {coeffs[2]:.3f}*(t-{x[i]}) + {coeffs[3]:.3f}")

# 输出三次样条插值的分段多项式函数
print("\nCubic Spline Interpolation piecewise polynomials:")
for i in range(len(x) - 1):
    coeffs = spline_interpolator.c[:, i]
    print(f"Interval [{x[i]}, {x[i+1]}]:")
    print(f"  {coeffs[0]:.3f}*(t-{x[i]})^3 + {coeffs[1]:.3f}*(t-{x[i]})^2 + {coeffs[2]:.3f}*(t-{x[i]}) + {coeffs[3]:.3f}")


# 定义积分区间
a, b = 0.15, 0.18

# 计算指定区间的积分
integral_hermite, _ = quad(hermite_interpolator, a, b)
integral_spline, _ = quad(spline_interpolator, a, b)

print(f"Integral of Hermite interpolation from {a} to {b}: {integral_hermite:.4f}")
print(f"Integral of Cubic Spline interpolation from {a} to {b}: {integral_spline:.4f}")


# 在区间[a, b]内找到最小值点
res_hermite = minimize_scalar(hermite_interpolator, bounds=(a, b), method='bounded')
res_spline = minimize_scalar(spline_interpolator, bounds=(a, b), method='bounded')

print(f"Minimum y value for Hermite interpolation in [{a}, {b}]: {res_hermite.fun:.4f} at x = {res_hermite.x:.4f}")
print(f"Minimum y value for Cubic Spline interpolation in [{a}, {b}]: {res_spline.fun:.4f} at x = {res_spline.x:.4f}")

# 在某一点计算斜率
point = 6
slope_hermite = hermite_interpolator.derivative()(point)
slope_spline = spline_interpolator.derivative()(point)

print(f"Slope of Hermite interpolation at x = {point}: {slope_hermite:.4f}")
print(f"Slope of Cubic Spline interpolation at x = {point}: {slope_spline:.4f}")

# 绘图
plt.plot(x, y, 'o', label='Data Points')
plt.plot(x_new, y_hermite, '-', label='Hermite Interpolation')
plt.plot(x_new, y_spline, '--', label='Cubic Spline Interpolation')
plt.legend()
plt.title('Comparison of Hermite and Cubic Spline Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
