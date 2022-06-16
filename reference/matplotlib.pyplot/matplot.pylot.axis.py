"""
matplotlib.pyplot.axis(*args, emit=True, **kwargs):
获取或设置一些轴属性的便利方法。

Call signatures:
xmin, xmax, ymin, ymax = axis()
xmin, xmax, ymin, ymax = axis([xmin, xmax, ymin, ymax])
xmin, xmax, ymin, ymax = axis(option)
xmin, xmax, ymin, ymax = axis(**kwargs)

Parameters:
xmin, xmax, ymin, ymax:float, optional
    要设置的轴限制。
    这也可以通过以下方式实现:
        ax.set(xlim=(xmin, xmax), ylim=(ymin, ymax))
option:bool or str
    如果是bool，打开或关闭轴线和标签。
    如果是一个字符串，可能的值是:
        'on':开启轴线和标签。与True相同。
        'off':关闭轴线和标签。与False相同。
        'equal':通过改变轴的限制来设置等比例（即让圆圈变成圆形）。
            这与ax.set_aspect('equal', adjustable='datalim')相同。
            在这种情况下，明确的数据限制可能不会被尊重。
        'scaled':通过改变绘图框的尺寸来设置等比例（即让圆圈变成圆形）。
            这与ax.set_aspect('equal', adjustable='box', anchor='C')相同。
            此外，进一步的自动缩放功能将被禁用。
        'tight':设置足够大的限制以显示所有数据，然后禁用进一步的自动缩放。
        'auto':自动缩放（用数据填充图框）。
        'image':'scaled' 轴限制等于数据限制。
        'square'
            方形图；与'scaled'类似，但最初强制xmax-xmin == ymax-ymin。
emit:bool, default: True
    观察者是否被通知轴的极限变化。
    这个选项会传递给set_xlim和set_ylim。
Returns:
    xmin, xmax, ymin, ymax:float
    轴限制。

"""