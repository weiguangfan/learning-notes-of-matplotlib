"""
显示如何连接到按键事件。

注意

这个例子锻炼了Matplotlib的交互能力，这将不会出现在静态文档中。
请在你的机器上运行这段代码以查看交互性。

你可以复制和粘贴个别部分，或者使用页面底部的链接下载整个例子。



"""
import sys
import numpy as np
import matplotlib.pyplot as plt


def on_press(event):
    print('press',event.key)
    sys.stdout.flush()
    if event.key == 'x':
        visible = xl.get_visible()
        xl.set_visible(not visible)
        fig.canvas.draw()


np.random.seed(19680801)
fig,ax = plt.subplots()
fig.canvas.mpl_connect('key_press_event',on_press)
ax.plot(np.random.rand(12),np.random.rand(12),'go')
xl = ax.set_xlabel('easy come, easy go')
ax.set_title('Press a key')
plt.show()
