import numpy as np

def ic_1_1(x, y, a, n):
    x1 = y
    y1 = a[n] * y * (1- x * x) - x
    x = x1
    y = y1
    return x, y


if __name__ == "__main__":
    a_values = [0.04, 0.05, 0.06]

    n = 1
    j = 1
    x_start = [0.2, 0.2, 0.4, 0.4]
    y_start = [0.2, 0.4, 0.4, 0.2]

    # x = x_start[j]
    # y = y_start[j]
    # for mi in range(0, 20):
    #     x, y = ic_1_1(x, y, a_values, n)  # next_step：更新x y的值
    #     # plot
    # j += 1

    while (n <= 3): # 遍历所有 a 值
        while (j <= 4): # 遍历所有x_start 和 y_start
            x = x_start[j]
            y = y_start[j]
            for mi in range(0, 20):
                x, y = ic_1_1(x, y, a_values, n)  # next_step：更新x y的值
                # plot
            j += 1
        n += 1
        j = 1
        # clearDiagram()
    # exit()

