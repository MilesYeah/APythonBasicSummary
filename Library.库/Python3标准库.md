Python3标准库



## 文本
1. string：通用字符串操作
1. re：正则表达式操作
1. difflib：差异计算工具
1. textwrap：文本填充
1. unicodedata：Unicode字符数据库
1. stringprep：互联网字符串准备工具
1. readline：GNU按行读取接口
1. rlcompleter：GNU按行读取的实现函数

## 二进制数据
1. struct：将字节解析为打包的二进制数据
1. codecs：注册表与基类的编解码器

## 数据类型
1. datetime：基于日期与时间工具
1. calendar：通用月份函数
1. collections：容器数据类型
1. collections.abc：容器虚基类
1. heapq：堆队列算法
1. bisect：数组二分算法
1. array：高效数值数组
1. weakref：弱引用
1. types：内置类型的动态创建与命名
1. copy：浅拷贝与深拷贝
1. pprint：格式化输出
1. reprlib：交替repr()的实现

## 数学
1. numbers：数值的虚基类
1. math：数学函数
1. cmath：复数的数学函数
1. decimal：定点数与浮点数计算
1. fractions：有理数
1. random：生成伪随机数

## 函数式编程
1. itertools：为高效循环生成迭代器
1. functools：可调用对象上的高阶函数与操作
1. operator：针对函数的标准操作

## 文件与目录
1. os.path：通用路径名控制
1. fileinput：从多输入流中遍历行
1. stat：解释stat()的结果
1. filecmp：文件与目录的比较函数
1. tempfile：生成临时文件与目录
1. glob：Unix风格路径名格式的扩展
1. fnmatch：Unix风格路径名格式的比对
1. linecache：文本行的随机存储
1. shutil：高级文件操作
1. macpath：Mac OS 9路径控制函数

## 持久化
1. pickle：Python对象序列化
1. copyreg：注册机对pickle的支持函数
1. shelve：Python对象持久化
1. marshal：内部Python对象序列化
1. dbm：Unix“数据库”接口
1. sqlite3：针对SQLite数据库的API 2.0

## 压缩
1. zlib：兼容gzip的压缩
1. gzip：对gzip文件的支持
1. bz2：对bzip2压缩的支持
1. lzma：使用LZMA算法的压缩
1. zipfile：操作ZIP存档
1. tarfile：读写tar存档文件

## 文件格式化
1. csv：读写CSV文件
1. configparser：配置文件解析器
1. netrc：netrc文件处理器
1. xdrlib：XDR数据编码与解码
1. plistlib：生成和解析Mac OS X .plist文件

## 加密
1. hashlib：安全散列与消息摘要
1. hmac：针对消息认证的键散列

## 操作系统工具
1. os：多方面的操作系统接口
1. io：流核心工具
1. time：时间的查询与转化
1. argparser：命令行选项、参数和子命令的解析器
1. optparser：命令行选项解析器
1. getopt：C风格的命令行选项解析器
1. logging：Python日志工具
1. logging.config：日志配置
1. logging.handlers：日志处理器
1. getpass：简易密码输入
1. curses：字符显示的终端处理
1. curses.textpad：curses程序的文本输入域
1. curses.ascii：ASCII字符集工具
1. curses.panel：curses的控件栈扩展
1. platform：访问底层平台认证数据
1. errno：标准错误记号
1. ctypes：Python外部函数库

## 并发
1. threading：基于线程的并行
1. multiprocessing：基于进程的并行
1. concurrent：并发包
1. concurrent.futures：启动并行任务
1. subprocess：子进程管理
1. sched：事件调度
1. queue：同步队列
1. select：等待I/O完成
1. dummy_threading：threading模块的替代（当_thread不可用时）
1. _thread：底层的线程API（threading基于其上）
1. _dummy_thread：_thread模块的替代（当_thread不可用时）

## 进程间通信
1. socket：底层网络接口
1. ssl：socket对象的TLS/SSL填充器
1. asyncore：异步套接字处理器
1. asynchat：异步套接字命令/响应处理器
1. signal：异步事务信号处理器
1. mmap：内存映射文件支持

## 互联网
1. email：邮件与MIME处理包
1. json：JSON编码与解码
1. mailcap：mailcap文件处理
1. mailbox：多种格式控制邮箱
1. mimetypes：文件名与MIME类型映射
1. base64：RFC 3548：Base16、Base32、Base64编码
1. binhex：binhex4文件编码与解码
1. binascii：二进制码与ASCII码间的转化
1. quopri：MIME quoted-printable数据的编码与解码
1. uu：uuencode文件的编码与解码

## HTML与XML
1. html：HTML支持
1. html.parser：简单HTML与XHTML解析器
1. html.entities：HTML通用实体的定义
1. xml：XML处理模块
1. xml.etree.ElementTree：树形XML元素API
1. xml.dom：XML DOM API
1. xml.dom.minidom：XML DOM最小生成树
1. xml.dom.pulldom：构建部分DOM树的支持
1. xml.sax：SAX2解析的支持
1. xml.sax.handler：SAX处理器基类
1. xml.sax.saxutils：SAX工具
1. xml.sax.xmlreader：SAX解析器接口
1. xml.parsers.expat：运用Expat快速解析XML

## 互联网协议与支持
1. webbrowser：简易Web浏览器控制器
1. cgi：CGI支持
1. cgitb：CGI脚本反向追踪管理器
1. wsgiref：WSGI工具与引用实现
1. urllib：URL处理模块
1. urllib.request：打开URL连接的扩展库
1. urllib.response：urllib模块的响应类
1. urllib.parse：将URL解析成组件
1. urllib.error：urllib.request引发的异常类
1. urllib.robotparser：robots.txt的解析器
1. http：HTTP模块
1. http.client：HTTP协议客户端
1. ftplib：FTP协议客户端
1. poplib：POP协议客户端
1. imaplib：IMAP4协议客户端
1. nntplib：NNTP协议客户端
1. smtplib：SMTP协议客户端
1. smtpd：SMTP服务器
1. telnetlib：Telnet客户端
1. uuid：RFC4122的UUID对象
1. socketserver：网络服务器框架
1. http.server：HTTP服务器
1. http.cookies：HTTPCookie状态管理器
1. http.cookiejar：HTTP客户端的Cookie处理
1. xmlrpc：XML-RPC服务器和客户端模块
1. xmlrpc.client：XML-RPC客户端访问
1. xmlrpc.server：XML-RPC服务器基础
1. ipaddress：IPv4/IPv6控制库

## 多媒体
1. audioop：处理原始音频数据
1. aifc：读写AIFF和AIFC文件
1. sunau：读写Sun AU文件
1. wave：读写WAV文件
1. chunk：读取IFF大文件
1. colorsys：颜色系统间转化
1. imghdr：指定图像类型
1. sndhdr：指定声音文件类型
1. ossaudiodev：访问兼容OSS的音频设备

## 国际化
1. gettext：多语言的国际化服务
1. locale：国际化服务

## 编程框架
1. turtle：Turtle图形库
1. cmd：基于行的命令解释器支持
1. shlex：简单词典分析

## Tk图形用户接口
1. tkinter：Tcl/Tk接口
1. tkinter.ttk：Tk主题控件
1. tkinter.tix：Tk扩展控件
1. tkinter.scrolledtext：滚轴文本控件

## 开发工具
1. pydoc：文档生成器和在线帮助系统
1. doctest：交互式Python示例
1. unittest：单元测试框架
1. unittest.mock：模拟对象库
1. test：Python回归测试包
1. test.support：Python测试工具套件
1. venv：虚拟环境搭建

## 调试
1. bdb：调试框架
1. faulthandler：Python反向追踪库
1. pdb：Python调试器
1. timeit：小段代码执行时间测算
1. trace：Python执行状态追踪

## 运行时
1. sys：系统相关的参数与函数
1. sysconfig：访问Python配置信息
1. builtins：内置对象
1. __main__：顶层脚本环境
1. warnings：警告控制
1. contextlib：with状态的上下文工具
1. abc：虚基类
1. atexit：出口处理器
1. traceback：打印或读取一条栈的反向追踪
1. __future__：未来状态定义
1. gc：垃圾回收接口
1. inspect：检查存活的对象
1. site：址相关的配置钩子（hook）
1. fpectl：浮点数异常控制
1. distutils：生成和安装Python模块

## 解释器
1. code：基类解释器
1. codeop：编译Python代码

## 导入模块
1. imp：访问import模块的内部
1. zipimport：从ZIP归档中导入模块
1. pkgutil：包扩展工具
1. modulefinder：通过脚本查找模块
1. runpy：定位并执行Python模块
1. importlib：import的一种实施

## Python语言
1. parser：访问Python解析树
1. ast：抽象句法树
1. symtable：访问编译器符号表
1. symbol：Python解析树中的常量
1. token：Python解析树中的常量
1. keyword：Python关键字测试
1. tokenize：Python源文件分词
1. tabnany：模糊缩进检测
1. pyclbr：Python类浏览支持
1. py_compile：编译Python源文件
1. compileall：按字节编译Python库
1. dis：Python字节码的反汇编器
1. pickletools：序列化开发工具

## 其它
1. formatter：通用格式化输出

## Windows相关
1. msilib：读写Windows Installer文件
1. msvcrt：MS  VC++  Runtime的有用程序
1. winreg：Windows注册表访问
1. winsound：Windows声音播放接口

## Unix相关
1. posix：最常用的POSIX调用
1. pwd：密码数据库
1. spwd：影子密码数据库
1. grp：组数据库
1. crypt：Unix密码验证
1. termios：POSIX风格的tty控制
1. tty：终端控制函数
1. pty：伪终端工具
1. fcntl：系统调用fcntl()和ioctl()
1. pipes：shell管道接口
1. resource：资源可用信息
1. nis：Sun的NIS的接口
1. syslog：Unix  syslog程序库


