import numpy as np
import matplotlib.pyplot as plt

# 定义参数
a = 0.23
b = 0.75

# 定义迭代函数
def iterate_system(x, y, a, b):
    next_x = x**2 - y**2 - a
    next_y = 2*x*y - b
    return next_x, next_y

if __name__ == "__main__":
    # 初始条件
    x0, y0 = 0, 0  # 选择较为温和的初始条件

    # 迭代次数
    n_iter = 500

    # 存储迭代结果
    x_vals, y_vals = [x0], [y0]

    # 设置溢出检测的阈值
    max_val = 1e10  # 或者根据具体情况选择合适的值

    # 进行迭代
    for _ in range(n_iter):
        x_next, y_next = iterate_system(x_vals[-1], y_vals[-1], a, b)
        if abs(x_next) > max_val or abs(y_next) > max_val:
            print("Terminated early due to potential overflow.")
            break
        x_vals.append(x_next)
        y_vals.append(y_next)

    # 绘制相图
    plt.figure(figsize=(16, 12))
    plt.plot(x_vals, y_vals, '.')
    plt.title('Phase Portrait')
    plt.xlabel('$X_n$')
    plt.ylabel('$Y_n$')
    plt.grid(True)
    plt.show()