"""
matplotlib.artist.Artist.draw
Artist.draw(renderer)
    使用给定的渲染器绘制Artist （以及其子代）。

    如果artist是不可见的（Artist.get_visible返回False），则没有效果。

Parameters:
renderer:RendererBase subclass.

注意事项

该方法在Artist子类中被重写。

"""