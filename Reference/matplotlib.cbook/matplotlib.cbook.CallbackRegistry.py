"""
class matplotlib.cbook.CallbackRegistry(
                                        exception_handler=<function _exception_printer>,
                                        *,
                                        signals=None)
Bases: object

处理一组信号和回调的注册、处理、阻塞和断开连接的问题。

在实践中，
当不再需要回调时，
应该总是断开所有回调的连接，
以避免悬空引用（从而导致内存泄漏）。

然而，
Matplotlib中的实际代码很少这样做，
而且由于它的设计，
要放置这样的代码相当困难。

为了解决这个问题，
并防止这类内存泄漏，
我们只存储对绑定方法的弱引用，
所以当目标对象需要死亡时，
CallbackRegistry不会让它活着。


Parameters:
    exception_handler:callable,optinal
        如果不是 None，
        exception_handler 必须是一个以 Exception 作为单参数的函数。
        在CallbackRegistry.process过程中，
        它将与回调引发的任何异常一起被调用，
        并且可以重新引发该异常或以其他方式处理它。
    signals:list,optinal
        如果不是无，
        信号是这个注册表处理的信号列表：
        试图处理或连接到不在列表中的信号会抛出ValueError。
        默认情况下，无，不限制所处理的信号。

blocked(*, signal=None)
    阻止回调信号被处理。

    一个上下文管理器可以暂时阻止/禁用回调信号被注册的监听器处理。
    Parameters:signal:str, optional
        要屏蔽的回调信号。
        缺省是阻断所有信号。

connect(signal, func)
    注册func，当信号信号产生时被调用。

disconnect(cid)
    断开以callback id cid注册的回调的连接。

    如果这样的回调不存在，则不会产生错误。

process(s, *args, **kwargs)
    所有注册在s上接收回调的函数都将被调用，并带有*args和**kwargs。
"""


def oneat(x):
    print('eat', x)


def ondrink(x):
    print('drink', x)


from matplotlib.cbook import CallbackRegistry

callbacks = CallbackRegistry()

id_eat = callbacks.connect('eat',oneat)
id_drink = callbacks.connect('drink',ondrink)

print(callbacks.process('drink', 123))

print(callbacks.process('eat', 456))

print(callbacks.process('be merry', 456))  # nothing will be called

callbacks.disconnect(id_eat)
callbacks.process('eat',456)  # nothing will be called

with callbacks.blocked(signal='drink'):
    print(callbacks.process('drink', 123))   # nothing will be called

print(callbacks.process('drink', 123))

