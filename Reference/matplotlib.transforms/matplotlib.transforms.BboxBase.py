"""
class matplotlib.transforms.BboxBase(shorthand_name=None)

    Bases: TransformNode
    这个类是不可变的；Bbox是一个可变的子类。

    典型的表示方法是两个点，对它们的排序没有限制。
    我们提供了方便的属性来获取左、下、右和顶边以及宽度和高度，但这些并不明确地存储。

Parameters:
shorthand_name:str
    代表转换的 "名称 "的字符串。
    除了在DEBUG=True时提高str(transform)的可读性外，这个名字没有任何意义。
"""