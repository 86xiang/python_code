import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, np.pi * 4, 0.2)
y = np.sin(x)
plt.xlabel("y=sin(x)")
plt.ylabel("sin(x)")
plt.scatter(x, y, c='b', marker='x')
plt.show()
