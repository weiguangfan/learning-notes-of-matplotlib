"""
class matplotlib.axes.SubplotBase(fig, *args, **kwargs)
    Bases: object
    子图subplots的基类，
    子图是具有额外方法的Axes instances实例，
    以方便在一个图a figure中生成和操作一组轴 a set of Axes。
Parameters:
    fig:matplotlib.figure.Figure
    *args:tuple (nrows, ncols, index) or int
        图中的子图数组的尺寸是（nrows, ncols），index是被创建的子图的索引。
        index从左上角的1开始，向右增加。
        如果nrows, ncols和index都是个位数，
        那么args可以作为一个3位数传递（例如234代表（2, 3, 4））。
    **kwargs:
        关键字参数Keyword arguments被传递给轴（子）类构造函数the Axes (sub)class constructor.。


"""