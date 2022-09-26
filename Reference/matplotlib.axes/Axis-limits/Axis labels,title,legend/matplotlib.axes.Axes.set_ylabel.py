"""
Axes.set_ylabel(
                ylabel,
                fontdict=None,
                labelpad=None,
                *,
                loc=None,
                **kwargs)

设置Y轴的标签。
Parameters:
    ylabel:str
        标签文本。
    labelpad:float, default: rcParams["axes.labelpad"] (default: 4.0)
        以点为单位的轴线边界盒the Axes bounding box的间距，包括刻度线ticks和刻度线标签tick labels。
        如果没有，之前的值将保持不变。
    loc:{'bottom', 'center', 'top'}, default: rcParams["yaxis.labellocation"] (default: 'center')
        标签的位置。
        这是传递参数y和horizontalalignment的一种高级替代方法。
Other Parameters:
    **kwargs:Text properties
        Text properties文本属性控制标签的外观the appearance of the label。
"""