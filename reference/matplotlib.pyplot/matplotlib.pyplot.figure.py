"""
matplotlib.pyplot.figure(
                        num=None,
                        figsize=None,
                        dpi=None,
                        facecolor=None,
                        edgecolor=None,
                        frameon=True,
                        FigureClass=<class
                        'matplotlib.figure.Figure'>,
                        clear=False,
                        **kwargs):
创建一个新的图形，或激活一个现有的图形。
Parameters
    num: int or  str or Figure, optional
        图的唯一标识符。
        如果一个具有该标识符的图已经存在，这个图将被激活并返回。
        一个整数是指Figure.number属性，一个字符串是指图的标签。
        如果没有具有该标识符的图，或者没有给出num，那么将创建一个新的图，使之处于活动状态并返回。
        如果num是一个int，它将被用于Figure.number属性，
        否则，将使用一个自动生成的整数值（从1开始，每个新图都会递增）。
        如果num是一个字符串，图的标签和窗口标题将被设置为这个值。
    figsize: (float, float), default: rcParams["figure.figsize"] (default: [6.4, 4.8])
        宽度，高度，单位是英寸。
    dpi: float, default: rcParams["figure.dpi"] (default: 100.0)
        人物的分辨率，单位是每英寸点数。
    facecolor: color, default: rcParams["figure.facecolor"] (default: 'white')
        背景颜色。
    edgecolor: color, default: rcParams["figure.edgecolor"] （default: 'white'）
        边界颜色。
    frameon: bool, default: True
        如果为 "False"，则禁止绘制图框。
    FigureClass:  subclass of Figure
        可以选择使用一个自定义的Figure实例。
    clear: bool, default: False
        如果为True，并且图已经存在，那么它将被清除。
    tight_layout: bool or dict, default: rcParams["figure.autolayout"] (default: False)
        如果是False，则使用subplotpars。
        如果为True，则使用tight_layout调整子图参数，并使用默认的填充。
        当提供一个包含pad、w_pad、h_pad和rect这些键的dict时，默认的tight_layout的填充将被覆盖。
    constrained_layout: bool, default: rcParams["figure.constrained_layout.use"] （default: False)
        如果为True，使用约束布局来调整绘图元素的位置。
        与tight_layout类似，但设计得更加灵活。
        请参阅约束布局指南中的例子。(注意：与add_subplot或subplot2grid不起作用）。
    **kwargs: optional
        其他可能的参数见图。

Returns: Figure
    返回的Figure实例也将被传递给后台的new_figure_manager，
    它允许将自定义的Figure类挂到pyplot接口中。
    额外的 kwargs 将被传递给 Figure init 函数。

Notes
    如果你正在创建许多图形，请确保你明确地对不使用的图形调用 pyplot.close，因为这将使 pyplot 正确地清理内存。
    rcParams定义了默认值，可以在matplotlibrc文件中修改。
"""
# case1: Curve with error band
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch
"""
带有误差带的曲线
这个例子说明了如何在一条参数化的曲线周围绘制误差带。
一个参数化的曲线x(t), y(t)可以直接用plot绘制。
"""
N = 400
t = np.linspace(0, 2 * np.pi, N)
r = 0.5 + np.cos(t)
x, y = r * np.cos(t), r * np.sin(t)

fig, ax = plt.subplots()
ax.plot(x, y, "k")
ax.set(aspect=1)



def draw_error_band(ax, x, y, err, **kwargs):
    # Calculate normals via centered finite differences (except the first point
    # which uses a forward difference and the last point which uses a backward
    # difference).
    dx = np.concatenate([[x[1] - x[0]], x[2:] - x[:-2], [x[-1] - x[-2]]])
    dy = np.concatenate([[y[1] - y[0]], y[2:] - y[:-2], [y[-1] - y[-2]]])
    l = np.hypot(dx, dy)
    nx = dy / l
    ny = -dx / l

    # end points of errors
    xp = x + nx * err
    yp = y + ny * err
    xn = x - nx * err
    yn = y - ny * err

    vertices = np.block([[xp, xn[::-1]],
                         [yp, yn[::-1]]]).T
    codes = np.full(len(vertices), Path.LINETO)
    codes[0] = codes[len(xp)] = Path.MOVETO
    path = Path(vertices, codes)
    ax.add_patch(PathPatch(path, **kwargs))


axs = (plt.figure(constrained_layout=True)
       .subplots(1, 2, sharex=True, sharey=True))
errs = [
    (axs[0], "constant error", 0.05),
    (axs[1], "variable error", 0.05 * np.sin(2 * t) ** 2 + 0.04),
]
for i, (ax, title, err) in enumerate(errs):
    ax.set(title=title, aspect=1, xticks=[], yticks=[])
    ax.plot(x, y, "k")
    draw_error_band(ax, x, y, err=err,
                    facecolor=f"C{i}", edgecolor="none", alpha=.3)

plt.show()







