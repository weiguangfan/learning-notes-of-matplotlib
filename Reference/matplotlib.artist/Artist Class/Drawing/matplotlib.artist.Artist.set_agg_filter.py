"""
matplotlib.artist.Artist.set_agg_filter
Artist.set_agg_filter(filter_func)
    设置攻击性过滤器。
Parameters:
filter_func:callable
    一个过滤器函数，它接收一个（m, n, depth）浮点数组和一个dpi值，并返回一个（m, n, depth）数组和两个从图像左下角的偏移量
"""