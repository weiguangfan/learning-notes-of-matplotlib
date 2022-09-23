"""
class matplotlib.transforms.TransformNode(shorthand_name=None)

    Bases: object

    任何参与变换树并需要使其父辈无效或被无效的东西的基类。
    这包括不是真正的变换的类，比如边界框，因为有些变换依赖边界框来计算它们的值。

Parameters:
    shorthand_name:str
        代表转换的 "名称 "的字符串。
        除了在DEBUG=True时提高str(transform)的可读性外，这个名字没有任何意义。

"""