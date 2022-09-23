"""
class matplotlib.transforms.Bbox(
                                    points,
                                    **kwargs)
Bases: BboxBase
一个可变的边界框。

warning
我们建议总是明确指定忽略。
如果不这样做，可以通过访问你的Bbox的代码随时改变ignore的默认值，例如，使用ignore方法。

Parameters:
points:ndarray
    一个2x2的numpy数组，形式为[[x0, y0], [x1, y1]]。

"""
# Examples
# Create from known bounds
# 默认构造函数接受边界 "点"[[xmin, ymin], [xmax, ymax]]。
from matplotlib.transforms import Bbox

print(Bbox([[1, 1], [3, 7]]))

# 或者，可以从扁平化的点阵中创建一个Bbox，即所谓的 "extents"（xmin, ymin, xmax, ymax）。
print(Bbox.from_extents(1, 1, 3, 7))

# 或从 "边界"（xmin, ymin, width, height）。
print(Bbox.from_bounds(1, 1, 2, 6))

# Create from collections of points
# 累积Bboxs的 "空 "对象是null bbox，它是空集的替身。
print(Bbox.null())

# 将点添加到null bbox中，就可以得到这些点的bbox。
box = Bbox.null()
box.update_from_data_xy([[1,1]])
print(box)

box.update_from_data_xy([[2,3],[3,2]],ignore=False)
print(box)

# 设置ignore=True等同于从一个空的bbox重新开始。
box.update_from_data_xy([[1,1]],ignore=True)
print(box)

# Properties of the ``null`` bbox
# Bbox.null()当前的行为可能令人惊讶，因为它不具备 "空集 "的所有属性，因此在数学意义上，它的行为不像是一个 "零 "对象。
# 我们可能会在未来改变这一点（有一个废弃期）。

# 空bbox是交叉点的标识
print(Bbox.intersection(Bbox([[1, 1], [3, 7]]), Bbox.null()))

# 除了与自己一起，它返回完整的空间。
print(Bbox.intersection(Bbox.null(), Bbox.null()))

# 一个包含null的联合体将总是返回完整的空间（而不是另一个集合！）。
print(Bbox.union([Bbox([[0, 0], [0, 0]]), Bbox.null()]))
