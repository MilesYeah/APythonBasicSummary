
# ctypes — A foreign function library for Python


## 初见ctypes

Python 的 ctypes 要使用 C 函数，需要先将 C 编译成动态链接库的形式，即 Windows 下的 .dll 文件，或者 Linux 下的 .so 文件。先来看一下 ctypes 怎么使用 C 标准库。

Windows 系统下的 C 标准库动态链接文件为 msvcrt.dll (一般在目录 C:\Windows\System32 和 C:\Windows\SysWOW64 下分别对应 32-bit 和 64-bit，使用时不用刻意区分，Python 会选择合适的)

Linux 系统下的 C 标准库动态链接文件为 libc.so.6 (以 64-bit Ubuntu 系统为例， 在目录 /lib/x86_64-linux-gnu 下)

例如，以下代码片段导入 C 标准库，并使用 printf 函数打印一条消息，

```py
import platform
from ctypes import *

if platform.system() == 'Windows':
    libc = cdll.LoadLibrary('msvcrt.dll')
elif platform.system() =='Linux':
    libc = cdll.LoadLibrary('libc.so.6')
    
libc.printf('Hello ctypes!\n')
```

另外导入dll文件，还有其它方式如下，详细解释请参阅 ctypes module 相关文档，
```py
import platform
from ctypes import *

if platform.system() == 'Windows':
    libc = cdll.LoadLibrary('msvcrt.dll')
    #libc = windll.LoadLibrary('msvcrt.dll')  # Windows only
    #libc = oledll.LoadLibrary('msvcrt.dll')  # Windows only
    #libc = pydll.LoadLibrary('msvcrt.dll')
  
    #libc = CDLL('msvcrt.dll')
    #libc = WinDLL('msvcrt.dll')  # Windows only
    #libc = OleDLL('msvcrt.dll')  # Windows only
    #libc = PyDLL('msvcrt.dll')
elif platform.system() =='Linux':
    libc = cdll.LoadLibrary('libc.so.6')
    #libc = pydll.LoadLibrary('libc.so.6')

    #libc = CDLL('libc.so.6')
    #libc = PyDLL('libc.so.6')
    
libc.printf('Hello ctypes!\n')
```





## ctypes 数据类型

ctypes 作为 Python 和 C 联系的桥梁，它定义了专有的数据类型来衔接这两种编程语言。如下表，

ctypes type	|   C type	|   Python type
------------|-----------|--------------
c_bool	|   _Bool	|   bool (1)
c_char	|   char	|   1-character bytes object
c_wchar	|   wchar_t	|   1-character string
c_byte	|   char	|   int
c_ubyte	|   unsigned char	|   int
c_short	|   short	|   int
c_ushort	|   unsigned short	|   int
c_int	|   int	|   int
c_uint	|   unsigned int	|   int
c_long	|   long	|   int
c_ulong	|   unsigned long	|   int
c_longlong	|   __int64 or long long	|   int
c_ulonglong	|   unsigned __int64 or unsigned long long	|   int
c_size_t	|   size_t	|   int
c_ssize_t	|   ssize_t or Py_ssize_t	|   int
c_float	|   float	|   float
c_double	|   double	|   float
c_longdouble	|   long double	|   float
c_char_p	|   char * (NUL terminated)	|   bytes object or None
c_wchar_p	|   wchar_t * (NUL terminated)	|   string or None
c_void_p	|   void *	|   int or None


注：Python 中的类型，除了 None，int， long， Byte String，Unicode String 作为 C 函数的参数默认提供转换外，其它类型都必须显式提供转换。
* None：对应 C 中的 NULL
* int, long： 对应 C 中的 int，具体实现时会根据机器字长自动适配。
* Byte String：对应 C 中的一个字符串指针 char * ，指向一块内存区域。
* Unicode String ：对应 C 中一个宽字符串指针 wchar_t *，指向一块内存区域。

```py
import platform
from ctypes import *

if platform.system() == 'Windows':
    libc = cdll.LoadLibrary('msvcrt.dll')
elif platform.system() == 'Linux':
    libc = cdll.LoadLibrary('libc.so.6')

libc.printf('%s\n', 'here!')        # here!
libc.printf('%S\n', u'there!')      # there!
libc.printf('%d\n', 42)             # 42
libc.printf('%ld\n', 60000000)      # 60000000

#libc.printf('%f\n', 3.14)          #>>> ctypes.ArgumentError
#libc.printf('%f\n', c_float(3.14)) #>>> dont know why 0.000000
libc.printf('%f\n', c_double(3.14)) # 3.140000
```


