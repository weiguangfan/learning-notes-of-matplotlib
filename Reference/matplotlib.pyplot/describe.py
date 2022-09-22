"""
matplotlib.pyplot是matplotlib的一个基于状态的接口。
它提供了一种隐含的、类似MATLAB的绘图方式。
它还可以在你的屏幕上打开图形，
并充当图形GUI管理器。

pyplot主要用于交互式绘图和程序化绘图的简单案例。







"""
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0, 5, 0.1)
y = np.sin(x)
plt.plot(x, y)
plt.show()










