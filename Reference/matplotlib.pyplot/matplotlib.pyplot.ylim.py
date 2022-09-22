"""
matplotlib.pyplot.ylim(*args, **kwargs):
获取或设置当前轴的y-lim。

Call signatures:
bottom, top = ylim()
    返回当前ylim

ylim((bottom,top))
    将ylim设置为bottom,top

ylim(bottom,top)
    将ylim设置为bottom,top

设置限制可以关闭Y轴的自动缩放功能。

Returns：bottom, top
    一个新的Y轴限制的元组。
Notes：
    调用此函数时不带参数（例如 ylim() ），相当于在当前坐标轴上调用 get_ylim 的 pyplot 函数。
    调用这个函数时有参数，相当于在当前坐标轴上调用set_ylim的pyplot函数。
    不过所有的参数都会被传递。
"""



