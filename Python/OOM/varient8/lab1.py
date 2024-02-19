from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import numpy as np

class DynamicSystem(ABC):
    """定义一个抽象基类，供所有动态系统继承"""
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @abstractmethod
    def next_state(self, current_state):
        '''定义一个抽象方法，用于计算下一个状态。具体实现留给子类'''
        pass

    def plot_phase_diagram(self, initial_states, iterations, title):
        """
        绘制系统的相位图。该方法适用于所有继承自本类的动态系统
        :param initial_states: 代表一组初始状态
        :param iterations: 迭代次数
        :param title: 图表标题
        """
        for state in initial_states:
            # 对每个初始状态进行迭代，绘制其轨迹
            trajectory = [state]
            for _ in range(iterations):
                # 计算并追加轨迹的下一个点
                trajectory.append(self.next_state(trajectory[-1]))
            trajectory = np.array(trajectory)
            plt.plot(trajectory[:, 0], trajectory[:, 1], '-o')
            # print("initial state : ", state, "trajectory: ", trajectory)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(title)
        plt.grid(True)
        plt.show()

class ScalarDynamicSystem(DynamicSystem):
    """
    定义一个处理标量形式的具体动态系统类
    """
    def next_state(self, current_state):
        x, y = current_state
        x_next = (x * (self.a - x - y)) / 3
        y_next = (y * (self.b * y - x)) / 3
        return np.array([x_next, y_next])

class FixedPointsFinder:
    def __init__(self, dynamic_system):
        self.dynamic_system = dynamic_system

    def find_fixed_points(self, search_space): # TODO: 搜索算法可能有错误，只能搜出(0,0)
        """在给定的搜索范围内寻找不动点"""
        fixed_points = []
        for point in search_space:
            next_point = self.dynamic_system.next_state(point)
            # 对于实际系统，可能需要根据系统的特性调整 atol 的值
            if np.allclose(point, next_point, atol=1e-4):
                # 在确认为不动点之前，进一步验证点是否真的稳定
                is_fixed = True
                for _ in range(10):  # 确认连续多次迭代后，点保持不变
                    next_point = self.dynamic_system.next_state(next_point)
                    if not np.allclose(point, next_point, atol=1e-4):
                        is_fixed = False
                        break
                if is_fixed:
                    fixed_points.append(point)
        return fixed_points

if __name__ == "__main__":
    """
    绘制 varient 8 的相位图；寻找系统的不动点。
    TODO：写一个类处理矩阵-向量的输入
    """
    a_values = [5.0, 5.1]
    b_values = [3.0, 3.1]
    # 初值点（[x_start, y_start]）
    initial_states = [
        np.array([1.4, 0.9])
        , np.array([0.5, 0.2])
        , np.array([1.0, 0.5])
        , np.array([1.5, 1.2])
        , np.array([2.4, 0.9])
        , np.array([3.4, 0.9]) # OK
        , np.array([0, 0])  # OK 不动点
        # , np.array([0, 1.2])  # No, y -> 无穷
        , np.array([1.4, 0])  # OK。x 会趋近于 a-3；但是如果 x_start > a 则系统发散！
        # ,np.array([0, 1.2]) # No, x 不能为0
        # ,np.array([1.5, 0]) # No, y 不能为 0
        ,np.array([1.25, 0.75])
    ]

    for a in a_values:
        for b in b_values:
            ds = ScalarDynamicSystem(a, b)
            title = f"Phase Diagram for a={a}, b={b}"
            ds.plot_phase_diagram(initial_states, 20, title)
            # 创建不动点查找器实例，并在指定搜索范围内查找不动点
            finder = FixedPointsFinder(ds)
            search_space = [np.array([x, y]) for x in np.linspace(0, 5, 50) for y in np.linspace(0, 5, 50)]
            fixed_points = finder.find_fixed_points(search_space)
            print(f"Fixed Points for a={a}, b={b}:", fixed_points)
