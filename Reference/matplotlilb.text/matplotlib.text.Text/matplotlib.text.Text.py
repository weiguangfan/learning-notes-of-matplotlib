"""
在图中a figure包括文本 text的类。

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

处理窗口 window或数据坐标data coordinates中的文本的存储storing和绘制 drawing。

在x, y处创建一个带有字符串文本string text的Text实例。

The text文本根据horizontalalignment（默认：'left'）和verticalalignment（默认：'bottom'），
相对于锚点anchor point（x，y）进行对齐。
参见文本对齐方式。

虽然文本Text接受 "label标签 "关键字参数，
但默认情况下，
它不会被添加到图例的句柄中 the handles of a legend.。

有效的关键字参数是：
Property                                              Description
agg_filter                                            一个过滤函数，它接收一个（m, n, 3）浮点数组和一个dpi值，并返回一个（m, n, 3）数组和两个从图像左下角的偏移量
alpha                                                 scalar or None
animated                                              bool
backgroundcolor                                       color
bbox                                                  dict with properties for patches.FancyBboxPatch
clip_box                                              unknown
clip_on                                               unknown
clip_path                                             unknown
color or c                                            color
figure                                                Figure
fontfamily or family                                  {FONTNAME, 'serif', 'sans-serif', 'cursive', 'fantasy', 'monospace'}
fontproperties or font or font_properties             font_manager.FontProperties or str or pathlib.Path
fontsize or size                                      float or {'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'}
fontstretch or stretch                                {a numeric value in range 0-1000, 'ultra-condensed', 'extra-condensed', 'condensed', 'semi-condensed', 'normal', 'semi-expanded', 'expanded', 'extra-expanded', 'ultra-expanded'}


fontstyle or style                                    {'normal', 'italic', 'oblique'}
fontvariant or variant                                {'normal', 'small-caps'}
fontweight or weight                                  {a numeric value in range 0-1000, 'ultralight', 'light', 'normal', 'regular', 'book', 'medium', 'roman', 'semibold', 'demibold', 'demi', 'bold', 'heavy', 'extra bold', 'black'}

gid                                                   str
horizontalalignment or ha                             {'left', 'center', 'right'}
in_layout                                             bool
label                                                 object
linespacing                                           float (multiple of font size)

math_fontfamily                                       str
mouseover                                             bool
multialignment or ma                                  {'left', 'right', 'center'}
parse_math                                            bool
path_effects                                          AbstractPathEffect
picker                                                None or bool or float or callable
position                                              (float, float)
rasterized                                            bool
rotation                                              float or {'vertical', 'horizontal'}
rotation_mode                                         {None, 'default', 'anchor'}

sketch_params                                         (scale: float, length: float, randomness: float)
snap                                                  bool or None
text                                                  object
transform                                             Transform
transform_rotates_text                                bool
url                                                   str
usetex                                                bool or None
verticalalignment or va                               {'bottom', 'baseline', 'center', 'center_baseline', 'top'}
visible                                               bool
wrap                                                  bool
x                                                     float
y                                                     float
zorder                                                float

"""