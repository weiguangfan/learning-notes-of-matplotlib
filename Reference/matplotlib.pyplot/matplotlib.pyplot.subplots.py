"""
matplotlib.pyplot.subplots(
                            nrows=1,
                            ncols=1,
                            *,
                            sharex=False,
                            sharey=False,
                            squeeze=True,
                            subplot_kw=None,
                            gridspec_kw=None,
                            **fig_kw):

创建 a figure和 a set of subplots。
这个实用的包装器使得在一次调用中就能方便地创建subplots的普通布局，包括包围的 figure object。
Parameters
    nrows, ncols: int, default: 1
        子图网格的行数/列数。
    sharex, sharey: bool or {'none', 'all', 'row', 'col'}，default: False
        控制x轴（sharex）或y轴（sharey）之间的属性共享。
            True or 'all'：x轴或y轴将在所有子图中共享。
            False or 'none'：每个子图的x轴或y轴将是独立的。
            'row': 每个子图的行将共享一个x轴或y轴。
            'col': 每个子图的列将共享一个x轴或y轴。
            当子图有一个沿列共享的x轴时，只创建底部子图的x刻度线标签。
            同样地，当子图沿着一行共享y轴时，只创建第一列子图的y刻度标签。
            要想以后打开其他子图的刻度线标签，请使用tick_params。
            当子图有一个有单位的共享轴时，调用set_units将用新的单位更新每个轴。
    squeeze: bool，default: True
        如果是True，则从返回的坐标轴数组中挤出额外的尺寸。
            如果只构建了一个子图（nrows=ncols=1），返回的单个Axes对象是一个标量。
            对于Nx1或1xM的子图，返回的对象是一个由Axes对象组成的一维numpy对象阵列。
            对于NxM，N>1和M>1的子图将作为一个二维数组返回。
        如果是False，则完全不进行挤压：
            返回的Axes对象总是一个包含Axes实例的二维数组，即使它最终是1x1。
    subplot_kw: dict, optional
        含关键字的字典，传递给add_subplot的调用，用于创建每个子图。
    gridspec_kw: dict, optional
        含有关键字的Dict，传递给GridSpec构造函数，用于创建子图所处的网格。
    **fig_kw
        所有额外的关键字参数将被传递给pyplot.figure调用。

Returns
    fig: Figure
    ax: axes.Axes or array of Axes
        ax可以是一个单一的Axes对象，或者是一个Axes对象的数组（如果创建了多个子图）。
        结果数组的尺寸可以用squeeze关键字控制，见上文。
    处理返回值的典型习惯是:
        # 将变量ax用于单个a轴
        fig, ax = plt.subplots()

        # 将可变轴axs用于多个轴
        fig, axs = plt.subplots(2, 2)

        # 对多个轴使用元组解包
        fig, (ax1, ax2) = plt.subplots(1, 2)
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

        ax和复数axs的名称优先于axes，因为对于后者，不清楚它是指单个axes实例还是这些实例的集合。
"""
import numpy as np
import matplotlib.pylab as plt
# First create some toy data:
x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)

# Create just a figure and only one subplot
# fig, ax = plt.subplots()
# ax.plot(x, y)
# ax.set_title('Simple plot')

# Create two subplots and unpack the output array immediately
# f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
# ax1.plot(x, y)
# ax1.set_title('Sharing Y axis')
# ax2.scatter(x, y)

# Create four polar axes and access them through the returned array
# fig, axs = plt.subplots(2, 2, subplot_kw=dict(projection="polar"))
# axs[0, 0].plot(x, y)
# axs[1, 1].scatter(x, y)

# Share a X axis with each column of subplots
# plt.subplots(2, 2, sharex='col')

# Share a Y axis with each row of subplots
# plt.subplots(2, 2, sharey='row')

# Share both X and Y axes with all subplots
# plt.subplots(2, 2, sharex='all', sharey='all')

# Note that this is the same as
# plt.subplots(2, 2, sharex=True, sharey=True)

# Create figure number 10 with a single subplot
# and clears it if it already exists.
# fig, ax = plt.subplots(num=10, clear=True)

plt.show()

