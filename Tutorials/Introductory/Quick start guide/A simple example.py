"""
Matplotlib将你的数据绘制在Figure上（例如，窗口、Jupyter部件等），每个Figure可以包含一个或多个Axes，这是一个可以用x-y坐标（或极坐标图中的theta-r，3D图中的x-y-z等）来指定点的区域。
创建带有坐标轴的图的最简单方法是使用 pyplot.subplots。
然后我们可以使用Axes.plot在坐标轴上绘制一些数据。

"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

fig,ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([1,2,3,4],[1,4,2,3])  # Plot some data on the axes.
plt.show()