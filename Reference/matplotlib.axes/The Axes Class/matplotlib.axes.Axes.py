"""
class matplotlib.axes.Axes(
                            fig,
                            rect,
                            *,
                            facecolor=None,
                            frameon=True,
                            sharex=None,
                            sharey=None,
                            label='',
                            xscale=None,
                            yscale=None,
                            box_aspect=None,
                            **kwargs)

Bases: _AxesBase
The Axes包含大多数图形元素：Axis轴、Tick勾线、Line2D、Text文本、Polygon多边形等，并设置坐标系。

Axes实例通过callbacks属性支持回调，
该属性是一个CallbackRegistry实例。

你可以连接的事件是 "xlim_changed "和 "ylim_changed"，
回调将被func(ax)调用，ax是Axes实例。
Attributes:
    dataLim:Bbox
        包围轴线the Axes上显示的所有数据的边界框。
    viewLim:Bbox
        数据坐标中的视图限制。

在图形中建立一个轴。

Parameters:
    fig:Figure




"""


