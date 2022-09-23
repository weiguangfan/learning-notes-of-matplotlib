"""
class matplotlib.axis.Axis(
                            axes,
                            *,
                            pickradius=15)

    XAxis 和 YAxis 的基类。

Attributes:isDefault_label: bool
    axes:matplotlib.axes.Axes
        艺术家所在的Axes实例或None。
    major:matplotlib.axis.Ticker
        确定主要的刻度线位置和它们的标签格式。
    minor:matplotlib.axis.Ticker
        确定次要的刻度线位置和它们的标签格式。
    callbacks:matplotlib.cbook.CallbackRegistry
    label:Text
        轴的标签。
    labelpad:float
        轴标签和刻度线标签之间的距离。
        默认为rcParams["axes.labelpad"] （默认：4.0）=4。
    offsetText:Text
        一个文本对象，包含刻度线的数据偏移（如果有的话）。
    pickradius:float
        安全性测试的验收半径。
    majorTicks:list of Tick
        主要的刻度
    minorTicks:list of Tick
        次要的刻度

Parameters:
    axes：matplotlib.axes.Axes
        创建的轴Axis所属的轴Axes。
    pickradius:float
        安全性测试的验收半径。See also Axis.contains.
"""