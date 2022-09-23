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
        轴心是在图中建立的。
    rect:tuple (left, bottom, width, height).
        轴线是建立在矩形rect中的。
        rect是在图中的坐标。
    sharex, sharey:Axes, optional
        x或y轴与输入轴中的x或y轴共享。
    frameon:bool, default: True
        轴的框架是否可见。
    box_aspect:float, optional
        为Axes盒子设置一个固定的长宽比，即高度和宽度的比例。
        详见set_box_aspect。
    **kwargs
        其他可选的关键字参数:

Returns:
Axes:
新的Axes对象。

"""


