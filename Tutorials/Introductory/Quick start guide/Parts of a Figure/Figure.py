"""
整个图。
图记录了所有的子轴、一组 "特殊 "的艺术家（标题、图例、色条等），甚至是嵌套的子图。

创建一个新图的最简单方法是使用pyplot。

"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()  # an empty figure with no Axes
# fig,ax = plt.subplots()  # a figure with a single Axes
# fig,axs = plt.subplots(2,2)  # a figure with a 2x2 grid of Axes
"""
通常情况下，与图一起创建轴是很方便的，但你也可以在以后手动添加轴。
请注意，许多Matplotlib的后端支持图形窗口的缩放和平移。
"""
