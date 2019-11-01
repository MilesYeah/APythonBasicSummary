# Python 利用日志捕捉异常

Python的logging模块中exception可以用于捕获程序运行中的异常。

常用的方法是结合try except，在except中捕获运行异常。

其默认的logging等级为logging.ERROR。




```py
import logging
LOG_FILENAME = 'logging_example.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
 
logging.debug('This message should go to the log file')
 
try:
   run_my_stuff()
except:
   logging.exception('Got exception on main handler')
```

```py
DEBUG:root:This message should go to the log file
ERROR:root:Got exception on main handler
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
NameError: name 'run_my_stuff' is not defined
```
