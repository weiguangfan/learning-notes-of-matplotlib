"""
Axes.set_title(
                label,
                fontdict=None,
                loc=None,
                pad=None,
                *,
                y=None,
                **kwargs)
为 the Axes设置一个标题。

设置三个可用的轴的标题the three available Axes titles之一。
可用的标题在轴 the Axes上方的中心位置，与左边缘平齐，与右边缘平齐。
Parameters:
    label:str
        标题使用的文本
    fontdict:dict
        一个控制标题文本外观的字典，默认的字体是：
        {'fontsize': rcParams['axes.titlesize'],
         'fontweight': rcParams['axes.titleweight'],
         'color': rcParams['axes.titlecolor'],
         'verticalalignment': 'baseline',
         'horizontalalignment': loc}
    loc:{'center', 'left', 'right'}, default: rcParams["axes.titlelocation"] (default: 'center')
        设置哪个标题。
    y:float, default: rcParams["axes.titley"] (default: None)
        垂直轴Vertical Axes location的标题位置（1.0为顶部）。
        如果无（默认）和rcParams["axes.titley"]（默认：无）也是无，则自动确定y，以避免轴上的装饰器 decorators on the Axes。
    pad:float, default: rcParams["axes.titlepad"] (default: 6.0)
        标题 the title与轴线顶部 the top of the Axes的偏移量，单位是点。

Returns:Text
    representing the title代表标题的matplotlib text instance文本实例

Other Parameters:
**kwargs:Text properties
    其他关键字参数是text properties文本属性，有效文本属性的列表见文本Text。
"""