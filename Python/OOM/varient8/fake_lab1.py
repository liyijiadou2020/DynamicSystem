import numpy as np

def ic_1_1(x, y, a_values, b_values, i, j):
    x1 = (x * (a_values[i] - x - y)) / 3
    y1 = (y * (b_values[j] * y - x)) / 3
    x = x1
    y = y1
    return x, y


if __name__ == "__main__":
    a_values = [5.0, 5.1]
    b_values = [3.0, 3.1]

    n = 0 # 控制 x、y 的初值
    i = 0 # 控制 a 的取值
    j = 0 # 控制 b 的取值
    x_start = [0.2, 0.2, 0.4, 0.4]
    y_start = [0.2, 0.4, 0.4, 0.2]


    while (i < 2): # 取遍所有 a
        print("***", " i =", i, "***")
        while (j < 2): # 取遍所有 b
            print("---", " j =", j, "---")
            while (n < 4): # 取遍所有x_start 和 y_start
                print("===", " n =", n, "===")
                x = x_start[n]
                y = y_start[n]
                for mi in range(0, 20): # 对于每一种初值情况迭代 20 次
                    x, y = ic_1_1(x, y, a_values, b_values, i, j)
                    # print("迭代中... mi = ", mi, " (", x, ",", y, ")")
                    # plot
                n += 1
            j += 1
            n = 0
        i += 1
        j = 0
        # clearDiagram()
        print("\n\n")
    # exit()