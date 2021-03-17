

* [日志](https://docs.djangoproject.com/zh-hans/3.1/topics/logging/)

Logger 的配置都是在 setting.py 中配置的。





## 日志模块的配置
这将配置父 root 记录器，以向控制台处理程序发送 WARNING 级别及以上的消息。通过将级别调整为 INFO 或 DEBUG，可以显示更多的消息。这在开发过程中可能很有用。
```conf
# 把所有的日志信息输出到控制台。
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
             'propagate': True,
             'level': 'DEBUG',
        }
    },
}
```

```py
# 
import os

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': False,
        },
    },
}
```

该日志配置做了以下事情：
1. 识别配置为 'dictConfig 版本 1' 格式。目前，这是唯一的 dictConfig 格式版本。
2. 定义两个格式化程序：
   1. simple，输出日志级别名称（如 DEBUG）和日志信息。
   2. format 字符串是一个普通的 Python 格式化字符串，它描述了每个日志行要输出的细节。可以输出的完整细节列表可以在 Formatter Objects 中找到。
   3. verbose，输出日志级别名称、日志信息，以及生成日志信息的时间、进程、线程和模块。
3. 定义两个过滤器：
   1. project.logging.SpecialFilter，使用别名 special。如果这个过滤器需要额外的参数，它们可以作为过滤器配置字典中的附加键提供。在这种情况下，当实例化 SpecialFilter 时，参数 foo 将被赋予一个 bar 的值。
   2. django.utils.log.RequireDebugTrue，当 DEBUG 为 True 时，传递记录。
4. 定义两个处理程序：
    1. console，一个 StreamHandler，它将任何 INFO （或更高）消息打印到 sys.stderr。该处理程序使用 simple 输出格式。
    2. mail_admins，一个 AdminEmailHandler，它向网站 ADMINS 发送任何 ERROR （或更高）消息。该处理程序使用 special 过滤器。
5. 配置三个记录器。
    1. django，将所有信息传递给 console 处理程序。
    2. django.request，它将所有 ERROR 消息传递给 mail_admins 处理程序。此外，这个记录器被标记为 不 传播消息。这意味着写给 django.request 的日志信息不会被 django 日志处理程序处理。
    3. myproject.custom，它将所有 INFO 或更高等级的消息传递给两个处理程序——console 和 mail_admins。这意味着所有 INFO 级别（或更高）的消息将被打印到控制台；ERROR 和 CRITICAL 消息也将通过电子邮件输出。


```py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'filters': {
        'special': {
            '()': 'project.logging.SpecialFilter',
            'foo': 'bar',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['special']
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'myproject.custom': {
            'handlers': ['console', 'mail_admins'],
            'level': 'INFO',
            'filters': ['special']
        }
    }
}
```


## 使用 logging 模块


```py
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

def my_view(request, arg1, arg):
    ...
    if bad_mojo:
        # Log an error message
        logger.error('Something went wrong!')
```


### 为 logger 命名

```py
# Get an instance of a specific named logger
logger = logging.getLogger('project.interesting.stuff')
```


### 发起 logging 调用
logger 实例包含了每种默认日志级别的入口方法：
```py
logger.debug()
logger.info()
logger.warning()
logger.error()
logger.critical()
```
还有两种其他的调用方法：

* logger.log()：手动输出一条指定日志级别的日志消息。
* logger.exception()：创建一个包含当前异常堆栈帧的 ERROR 级别日志消息。
















## Django 的日志记录扩展
### Loggers
1. django

2. django.request
   1. 记录与处理请求有关的信息。5XX 的响应以 ERROR 消息的形式出现；4XX 的响应以 WARNING 消息的形式出现。记录在 django.security 记录器中的请求不会记录在 django.request 中。

3. django.server
   1. 记录与处理由 runserver 命令调用的服务器收到的请求有关的消息。HTTP 5XX 响应被记录为 ERROR 消息，4XX 响应被记录为 WARNING 消息，其他所有消息被记录为 INFO。

4. django.template
   1. 记录与模板渲染相关的消息。

5. django.db.backends
   1. 与代码与数据库互动有关的信息。例如，请求执行的每一条应用程序级别的 SQL 语句都会以 DEBUG 级别记录到这个记录器。

6. django.security.*
   1. 安全记录器将接收任何发生 SuspiciousOperation 和其他安全相关错误的消息。每个子类型的安全错误都有一个子记录器，包括所有 SuspiciousOperations。日志事件的级别取决于异常处理的位置。 大多数发生的事件被记录为警告，而任何到达 WSGI 处理程序的 SuspiciousOperation 将被记录为错误。例如，当客户端的请求中包含一个 HTTP Host 头，而这个头不符合 ALLOWED_HOSTS 时，Django 会返回一个 400 的响应，并且错误信息会被记录到 django.security.DisallowedHost 记录器中。

7. django.db.backends.schema
   1. 记录 migrations framework 对数据库进行模式变更时执行的 SQL 查询。请注意，它不会记录 RunPython 执行的查询。给这个记录器的消息在其额外的上下文中有 params 和 sql （但与 django.db.backends 不同，不是 duration）。这些值的含义与 django.db.backends 中的解释相同。

### Handlers

```py
class AdminEmailHandler(include_html=False, email_backend=None, reporter_class=None)
    send_mail(subject, message, *args, **kwargs)
```

### 过滤器
```py
class CallbackFilter(callback)
class RequireDebugFalse
class RequireDebugTrue
```


























