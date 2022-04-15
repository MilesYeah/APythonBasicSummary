# json序列化时，可以处理的数据类型有哪些？如何定制支持datetime类型？

1、可以处理的数据类型是 string、int、list、tuple、dict、bool、null
2、定制支持datetime类型
--------------------------官方文档的memo-----------------------------------------------
```py
>>> import json
>>> class ComplexEncoder(json.JSONEncoder):
...     def default(self, obj):
...         if isinstance(obj, complex):
...             return [obj.real, obj.imag]
...         return json.JSONEncoder.default(self, obj)
...
>>> dumps(2 + 1j, cls=ComplexEncoder)
    '[2.0, 1.0]'
>>> ComplexEncoder().encode(2 + 1j)
    '[2.0, 1.0]'
>>> list(ComplexEncoder().iterencode(2 + 1j))
    ['[', '2.0', ', ', '1.0', ']']
```
----------------------------------------------------------------------------------------
```py
import json
import datetime
ret = datetime.datetime.now()
class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return json.JSONEncoder.default(self, obj)

print(json.dumps(ret,cls=CJsonEncoder))
```

作者：SlashBoyMr_wang
链接：https://www.jianshu.com/p/7993d0e4e31c
来源：简书
简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。

