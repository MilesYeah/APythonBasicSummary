# Python 文档字符串(DocStrings)


DocStrings 文档字符串是一个重要工具，用于解释文档程序，帮助你的程序文档更加简单易懂。

我们可以在函数体的第一行使用一对三个单引号 ''' 或者一对三个双引号 """ 来定义文档字符串。

你可以使用 __doc__（注意双下划线）调用函数中的文档字符串属性。
```py
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
def function():
        ''' say something here！
        '''
        pass
 
print (function.__doc__) # 调用 doc
```

输出结果为：
```
 say something here！
```
