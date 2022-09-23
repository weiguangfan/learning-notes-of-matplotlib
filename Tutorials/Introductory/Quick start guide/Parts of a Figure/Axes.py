"""
Axes是一个附在图表上的艺术家，
它包含了一个用于绘制数据的区域，
通常包括两个（三个，如果是3D）Axis对象（注意Axes和Axis的区别），
它提供了刻度和刻度标签，
为Axes中的数据提供比例scale。

每个轴也有一个标题（通过set_title()设置），
一个X标签（通过set_xlabel()设置），
和一个Y标签（通过set_ylabel()设置）。

Axes class 轴类及其成员函数是使用OOP接口的主要切入点，
并在其上定义了大多数绘图方法（如上图所示的ax.plot()，使用了plot方法）。
"""


