"""
在图中包括文本的类。

class matplotlib.text.Text(
                            x=0,
                            y=0,
                            text='',
                            *,
                            color=None,
                            verticalalignment='baseline',
                            horizontalalignment='left',
                            multialignment=None,
                            fontproperties=None,
                            rotation=None,
                            linespacing=None,
                            rotation_mode=None,
                            usetex=None,
                            wrap=False,
                            transform_rotates_text=False,
                            parse_math=None, **kwargs)

Bases: Artist

处理窗口或数据坐标中的文本的存储和绘制。

在x, y处创建一个带有字符串文本的Text实例。

文本根据horizontalalignment（默认：'left'）和verticalalignment（默认：'bottom'），相对于锚点（x，y）进行对齐。
参见文本对齐方式。

虽然文本接受 "label标签 "关键字参数，但默认情况下，它不会被添加到图例的句柄中。

有效的关键字参数是：



"""