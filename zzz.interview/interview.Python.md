# Python "知识点"


## Python 有哪些数据类型？
* 整型
* 列表
* 元组
* 字典
* 字符串
* 集合
* 布尔




## 不可变对象和可变对象的区别？
* 可变对象：对象存放在地址中的值不会被改变
* 不可变对象：对象存放在地址中的值会直接改变




## 不可变对象和可变对象从内存出发说下有什么区别？

### 不可变对象
* Python 中的变量存放的是对象引用
* 不可变对象是指对象本身不可变
* 变的只是创建了新对象，然后变量改变了对象引用，指向了新对象，旧对象会被垃圾回收

### 可变对象
变的是原来对象的内容，不会创建新对象，而变量也是指向原对象




## 字符串是可变对象还是不可变对象？
不可变对象




## 有哪些可变对象，哪些不可变对象？
* 不可变对象：字符串、元组、整型
* 可变对象：数组、字典、集合




## 单例模式是什么？怎么实现
该模式的主要目的是确保某一个类只有一个实例存在

```py
def new(cls, *args, **kwargs):
    if cls.instance is None:
        cls.instance = super().__new__(cls)
        return cls.instance
```





## 什么是闭包？
在一个内部函数中，对外部作用域的变量进行引用，(并且一般外部函数的返回值为内部函数)，那么内部函数就被认为是闭包




## 什么是装饰器？
* 通过装饰器函数，来修改原函数的一些功能，使得原函数不需要修改。让原来函数执行之前和执行完后分别运行某些代码
* 将函数作为参数传递给另一个函数
* 可以通过 functools 的 wraps 来定义函数修饰器
* 常用场景：身份认证、日志记录、输入合理性检查以及缓存等多个领域中




## Python 的装饰器一般是用来干嘛？
可以直接用框架提供的装饰器，也可以自己写装饰器
一般会用到 pytest、allure 的装饰器，自己写的有
* 异常捕捉：会给自己封装的每个方法加上这个异常捕捉装饰器，如果调用的封装方法报错了，就会进入这个装饰器，捕捉到指定异常后，我会刷新页面，再次执行刚刚报错的封装方法，然后会记录一次失败日志
* 日志：一般自己封装的方法都希望有日志，那如果每个封装的方法里单独调用日志类就会显得很臃肿重复，所以可以用一个日志装饰器代替
* 前置操作：比如多个方法执行前都需要调用同一个方法，那可以将依赖方法写在装饰器中
* 后置操作：比如每次执行方法后都需要还原数据集，可以将清理操作写在装饰器中
* 权限校验：执行方法前先进行权限校验，校验通过才会允许执行方法




## 怎么用装饰器实现单例模式

### 使用函数装饰器实现单例

```py
def singleton(cls):
    _instance = {}

    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]
    return inner


@singleton
class Cls(object):
    def __init__(self):
        pass


cls1 = Cls()
cls2 = Cls()

print(id(cls1) == id(cls2))
```

### 使用类装饰器实现单例

```py
class Singleton(object):

    def __init__(self, cls):
        self._cls = cls
        self._instance = {}

    def __call__(self):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()
        return self._instance[self._cls]


@Singleton
class Cls2(object):
    def __init__(self):
        pass


cls1 = Cls2()
cls2 = Cls2()
print(id(cls1) == id(cls2))
```





## Python 的内存管理机制有哪些？
垃圾回收，引用计数，内存池机制





## Python 的垃圾回收机制了解吗？
* 垃圾回收是 Python 内存管理的一种方式
* 内存泄露是服务端不愿看到的一种情况，服务端一般是 7*24 小时运行的，如果一直存在内存泄露的情况，就会导致机器真正可用的内存资源很少，最后导致服务端性能下降
* 内存泄露是服务端代码设计有问题，导致一些不再使用的内存没有及时回收，而服务端又无法控制这块内存，导致整体可用内存减少
* 引用计数是垃圾回收充分不必要条件，当一个对象被引用的次数为0时，该对象就会被垃圾回收，可以通过 sys.getrefcount() 来查看对象的引用计数
* 引用计数不能自动处理循环引用、引用环的情况，因为循环引用需要通过不可达判定才能确认是否能回收，但可以手动调用垃圾回收来处理（gc.collect）
* 垃圾回收还提供了另外两种自动回收方式：标记清除和分代收集，可以有效处理循环引用、引用环的情况
* 分代回收一般分为三代，新生的对象更容易被垃圾回收，老对象更容易存活，当每一代到达自动垃圾回收的阈值之后，就会启动垃圾回收
* 调试内存泄露，可以通过 objgraph 包的 show_refs、backrefs 方法查看变量引用调用图




## Python 的迭代器和生成器的区别？
* 元组、集合、字典、列表都是可迭代对象，如果一个对象实现了 __iter__ 方法就是可迭代对象
* 可迭代对象可以通过 for 循环进行迭代，也可以通过 Iterable 来判断是否为可迭代对象
* 可迭代对象调用 iter() 方法就能得到迭代器，迭代器可以通过 next() 来得到下一个元素，从而支持遍历
* 生成器是一种特殊的迭代器，将列表生成式的 [] 改成 () 就是生成器了
* 通过列表生成式处理大量数据时可能会耗尽内存，这个时候用生成器就能节省内存，提高性能，因为每次只会计算一次结果
* 带 yield 关键字的函数是一个生成器，下次迭代会回到 yield 继续执行




## is 和 == 的区别？
* 比较操作符'=='表示比较对象间的值是否相等，默认会调用对象的 __eq__() 方法，而'is'表示比较对象的标识是否相等，即它们是否指向同一个内存地址。
* 比较操作符'is'效率优于'=='，因为'is'操作符无法被重载，执行'is'操作只是简单的获取对象的 ID，并进行比较；而'=='操作符则会递归地遍历对象的所有值，并逐一比较。




## 深拷贝和浅拷贝的区别？
* 浅拷贝和深拷贝只有在可变对象才会生效，不可变对象的赋值操作、浅拷贝、深拷贝的效果是一样的
* 浅拷贝中的元素，是原对象中子对象的引用，因此，如果原对象中的元素是可变的，改变其也会影响拷贝后的对象，存在一定的副作用。
* 深度拷贝则会递归地拷贝原对象中的每一个子对象，因此拷贝后的对象和原对象互不相关。
* 另外，深度拷贝中会维护一个字典，记录已经拷贝的对象及其 ID，来提高效率并防止无限递归的发生




## Python 的协程是什么
协程和多线程的区别，主要在于两点
* 一是协程为单线程
* 二是协程由用户决定，在哪些地方交出控制权，切换到下一个任务

协程的写法更加简洁清晰，把 async / await 语法和 create_task 结合来用

对于中小级别的并发需求已经毫无压力

写协程程序的时候，你的脑海中要有清晰的事件循环概念，知道程序在什么时候需要暂停、等待 I/O，什么时候需要一并执行到底

```py
import asyncio

async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print(f'OK {url}')

async def main(urls):
    tasks = [asyncio.create_task(crawl_page(url)) for urls]
    for task in tasks:
        await task


%time asyncio.run(main(['url_1', 'url_2', 'url_3', 'url]

##########
输出
##########
```

* await asyncio.sleep(sleep_time) 会在这里休息若干秒
* asyncio.create_task() 来创建任务
* await task 执行协程，进入被调用的协程函数
* asyncio.run(main()) 触发运行
* asyncio.wait() 等待 task 来完成




## Python 的 GIL 是什么
* 全局解释器锁，诞生于 Python 解释器 CPython 的一个术语
* 每一个 Python 线程，在 CPython 解释器中执行时，都会先锁住自己的线程，阻止别的线程执行





## 为什么会有 GIL
* CPython 是通过引用技术来进行内存管理的，当某个变量引用技术为 0 的时候就会进行垃圾回收
* 当 Python 有多个线程同时引用一个变量时，可能会出现线程竞争导致内存污染，最终引用计数只增加1，可能会出现有一个线程无法正常访问这个变量
* 所以 GIL 诞生了，为了规避类似内存管理存在的复杂的竞争风险问题，也是因为 CPython 大量使用 C 语言库，但大部分 C 语言库都不是原生线程安全
* 但是 GIL 的存在并不能完全保证 Python 线程安全，因为它是为了方便 CPython 解释器层的开发者，而不是 Python 层的开发者




## 如何保证线程安全？(如何保证多个线程安全地访问竞争资源)
使用 lock 等工具

```py
n = 0
lock = threading.Lock()

def foo():
    global n
    with lock:
        n += 1

```





## n=256, n1=256, n is n1 是 false 还是 true？
true




## n=257, n1=257, n is n1 是 false 还是 true？
* 如果是不同代码块内容执行就是 false
* 如果是同代码块就是 true




## Python 代码，1-100怎么求和，一行代码怎么写？
```py
sum(range(1,101))
```



## 怎么判断这个字符串是否为字典里面的键？还有其他方法吗？
### 简单的方法

```py
"key" in dicts
"key" in dicts.keys()
```

### 复杂的方法一

```py
for i in dicts.keys():
    if i == "key":
        print(True)
```

### 复杂的方法二

```py
if dicts.get("key"):
    print(True)
```






## 个位十位百位千位都有1的数，怎么筛选出来？
简单粗暴

```py
for i in range(1, 1001):
    if str(i).find("1") ==0:
        print(i)
```





## range、xrange 的区别？
* xrange 是 python2 的东西，在 python3 里已弃用，range 在 python2、3 都有
* xrange 是一个类，返回的是一个 xrange 对象
* range 是一个函数，返回的是可迭代对象（range 对象），并不是一个列表【这里之前写的是列表！是错的！】




## search()、match() 方法有什么区别？
search 会搜索整个字符串进行匹配，

match 只会从第 0 个位置开始匹配，如果没有匹配成功，即使后面有对应的字符串也是失败

```py
# 匹配失败
print(re.match('super','insuperable'))


# 匹配成功

print(re.search('super','insuperable'))


# 匹配成功
print(re.match('super','superable'))
```





## Python 有用过哪些库？
标准库：
* os：提供多种操作系统功能接口的模块
* sys：提供 Python 运行环境的变量、函数的模块
* random：随机数
* math：数学
* datetime：基本的日期、时间类型
* time：时间的访问、转换
* pprint：美观打印
* hashlib：哈希库
* pathlib：文件系统路径库
* logging：日志工具
* json：JSON 解码、编码
* re：正则表达式

第三方库：
* requests：HTTP 请求
* pandas：分析结构化数据的库，比如 excel
* numpy：数学计算库
* pytest：单元测试框架库
* allure：测试报告库
* selenium：ui 自动化测试库
* appium：APP 自动化测试库




## Python 怎么把字典转成 json 字符串？
json.dumps()




## Python 读取一个文本文件要怎么实现？
* open(file)
* with open(file) as f




## Python 里面什么叫模块？
任何一个 .py 结尾的 python 文件




## from .. import 和 import 有什么区别？
* import 导入的最小单位是模块，不能是变量、函数名、类名
* from .. import 导入的最小单位可以是变量、函数名、类名




## Python 常见的异常？你遇到过得到异常有哪些？
* BaseException：所有异常的基类
* ValueError：无效参数值
* TypeError：无效参数类型
* SyntaxError：语法错误
* KeyError：找不到此键
* IndexError：找不到索引
* AttributeError：找不到属性
* ImportError：导入错误
* ZeroDivisionError：除0错误




## Python 中异常处理的语句有哪些？
* try：需要捕捉异常的代码块
* except：如果指定的异常发生了则执行
* else：如果没有异常发生则执行
* finally：无论是否捕捉到异常，都会执行下面代码

```py
try:
    <语句>
    #运行别的代码
except <名字>：
    <语句>
    #如果在try部份引发了'name'异常 except <名字>，<数据>: <语句>
    #如果引发了'name'异常，获得附加的数据
else: 
    <语句>
    #如果没有异常发生
finally:
    <语句>
    #无论是否有异常发生都执行

```




## Python 中单引号、双引号、三引号的应用场景？
* 首先，三种都能表示字符串
* 单引号和双引号一般就是表示字符串使用，如果需要字符串内嵌套字符串，就需要单双引号混合使用，当然也可以只用一种引号，但是要进行转义
* 三引号里面可以任意添加单引号、双引号的字符串，也能实现多行换行的字符串，这个单引号和双引号就做不到了
* 三引号也能作为一个多行注释来使用




## Python 2.0 和 3.0 有什么区别？大方面的总结
* 表达式
* print
* range
* 不等于操作
* 编码
* 中文字符字节数








# Python GIL

## Python 速度慢的两大原因

### 背景
相比 C/C++/JAVA，Python 确实慢，在一些特殊场景下，Python 比 C++ 慢100~200倍，由于速度慢的原因，很多公司的基础架构代码依然用C/C++开发
比如各大公司阿里/腾讯/快手的推荐引擎、搜索引擎、存储引擎等底层对性能要求高的模块


### 慢的原因
* 动态类型语言，边解释边执行
* 因为 GIL，无法利用多核 CPU 并发执行


## GIL 是什么？
* 全局解释器锁(英语：Global Interpreter Lock，缩写GIL)
* 是计算机程序设计语言解释器用于同步线程的一种机制，它使得任何时刻仅有一个线程在执行
* 即便在多核心处理器上，使用 GIL 的解释器也只允许同一时间执行一个线程
* GIL 会在线程进行 I/O 计算时释放





## 为什么有GIL这个东西?

### 简而言之
* Python 设计初期，为了规避并发问题引入了 GIL，现在想去除却去不掉了！
* GIL 简化了Python对共享资源的管理


### 为了解决多线程之间数据完整性和状态同步问题
Python中对象的管理，是使用引用计数器进行的，引用数为 0 则释放对象

线程A和线程B都引用了对象 obj，obj.ref_num=2，线程A和B都想撤销对obj的引用





## 怎样规避GIL带来的限制？
多线程 threading 机制依然是有用的，用于 IO 密集型计算
* 因为在 I/O(read,write,send,recvetc.)期间，线程会释放GIL，实现 CPU 和 IO 的并行
* 因此多线程用于 IO 密集型计算依然可以大幅提升速度
* 但是多线程用于 CPU 密集型计算时，只会更加拖慢速度

使用 multiprocessing 的多进程机制实现并行计算、利用多核CPU优势

为了应对 GIL 的问题，Python 提供了multiprocessing





## ref
* [Python "知识点"](https://www.yuque.com/poloyy/interview/kqid44)
* [Python GIL](https://www.yuque.com/poloyy/interview/kguc02)
* []()
* []()
* []()
* []()
* []()
* []()
