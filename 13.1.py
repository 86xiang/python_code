import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(6, 3))  # 创建绘图对象
x = np.arange(0, np.pi * 4, 0.01)
y = np.cos(2 * x)
plt.plot(x, y, color="b", ls='--', linewidth=2.0)
plt.xlabel("x")  # x轴文字
plt.ylabel("cos(2x)")  # y轴文字
plt.ylim(-1, 1)  # y轴范围
plt.title("y=cos(2x)")  # 图表标题
