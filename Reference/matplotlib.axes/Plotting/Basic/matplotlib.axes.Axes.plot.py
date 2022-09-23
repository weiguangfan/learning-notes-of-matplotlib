"""
Axes.plot(
            *args,
            scalex=True,
            scaley=True,
            data=None,
            **kwargs)
将y与x的关系绘制成线和/或标记。

Call signatures:
plot([x],y,[fmt],*,data=None,**kwargs)
plot([x],y,[fmt],[x2],y2,[fmt2],...,**kwargs)

点或线节点的坐标由x、y给出。

可选参数fmt是定义基本格式化的一种方便方式，如颜色、标记和线条样式。
它是一种快捷的字符串符号，在下面的注释部分有描述。
plot(x, y)        # plot x and y using default line style and color
plot(x, y, 'bo')  # plot x and y using blue circle markers
plot(y)           # plot y using x as index array 0..N-1
plot(y, 'r+')     # ditto, but with red plusses

你可以使用Line2D属性作为关键字参数来对外观进行更多控制。
线条属性和 fmt 可以混合使用。
下面的两个调用产生了相同的结果。

plot(x,y,'go--',linewidth=2,markersize=12)
plot(x,y,color='green',marker='o',linestyle='dashed',linewidth=2,markersize=12)

"""





