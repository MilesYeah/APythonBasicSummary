
# def func(a,b=[]) 这种写法有什么坑？

将可变对象作为默认参数，若多次调用时使用默认参数，默认参数会保留上次调用时的状态！
```py
>>> def add_to(v, l=[]):
...     l.append(v)
...     return l
...
>>> add_to(1)
[1]
>>> add_to(2)
[1, 2]
>>> ret = add_to(3)
>>> ret     # 我们以为，会返回[3]
[1, 2, 3]
>>>
```

如何改进，参数默认设为不可变类型None，在函数体中判断，如果是None则初始化为list
```py
>>> def add_to(v, l=None):
...     if l is None:
...         l = list()
...     l.append(v)
...     return l
...
>>> add_to(1)
[1]
>>> add_to(2)
[2]
>>> ret = add_to(3)
>>> ret
[3]
>>>
```