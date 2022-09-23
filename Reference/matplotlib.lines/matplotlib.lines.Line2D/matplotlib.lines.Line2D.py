"""
class matplotlib.lines.Line2D(
                                xdata,
                                ydata,
                                *,
                                linewidth=None,
                                linestyle=None,
                                color=None,
                                gapcolor=None,
                                marker=None,
                                markersize=None,
                                markeredgewidth=None,
                                markeredgecolor=None,
                                markerfacecolor=None,
                                markerfacecoloralt='none',
                                fillstyle=None,
                                antialiased=None,
                                dash_capstyle=None,
                                solid_capstyle=None,
                                dash_joinstyle=None,
                                solid_joinstyle=None,
                                pickradius=5,
                                drawstyle=None,
                                markevery=None,
                                **kwargs)

Bases: Artist

一条线--这条线既可以有连接所有顶点的实线样式，也可以在每个顶点有a marker。

此外，实线的绘制受到drawstyle的影响，
例如，人们可以用各种风格创建 "阶梯 "线。

创建一个Line2D实例，其x和y数据的序列为xdata, ydata。

额外的关键字参数是Line2D属性:
Property                           Description
agg_filter                         一个过滤器函数，它接收一个（m, n, 3）浮点数组和一个dpi值，并返回一个（m, n, 3）数组和两个从图像左下角的偏移量











"""

