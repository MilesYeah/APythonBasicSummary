# Python Coding Convention 编码规范


大部分不规范的编码，Pycharm都会提示出来，例如行长度太长，单词拼写错误，大小写不注意等。


## 标准文件模板
* 第1行：指定python解释器`#!/usr/bin/env python`
* 第2行：注明文档编码方式`# -*- coding: utf-8 -*-`
* 第3行：
* 第4行：模块注释`'a module to'`，事实上任何模块的第一个字符串都会被视为模块的文档注释
* 第5行：
* 第6行：`__author__: xxx.xx`作者信息



## 编码
1. 如无特殊情况, 文件一律使用 UTF-8 编码
2. 如无特殊情况, 文件头部必须加入#-*-coding:utf-8-*-标识


## 分号
1. 不要在行尾加分号。
2. 不要用分号将两条命令放在同一行。


## 行长度
* 每行代码尽量不超过 80 个字符(在特殊情况下可以略微超过 80 ，但最长不得超过 120)
* 使用括号连接多行，而不是使用反斜杠。
    ```py
    s = ('这是一个非常长的行，这是一个非常长的行，这是一个非常长的行，这是一个非常长的行，这是一个非常长的行，'
        '就这样吧！这一行到此结束！！')
    ```

    ```py
    def rftSendRecvRequest( rft, apiType, method, baseUrl, relPath=None, data=None, jsonData=True,  prop=None,
                            redirects=True, reqData=None, verify=False,
                            headersInput=None, **kwargs ):
        pass
    ```
* 例外：
  * 注释里的URL
    ```
    # See details at
    # http://www.example.com/us/developer/documentation/api/content/v2.0/csv_file_name_extension_full_specification.html
    ```
  * 超长模块导入便使用一行


## 括号
* 定义只有一个元素的元组需要使用括号和一个逗号，如`('v1',)`
* 宁缺毋滥的使用括号


## 缩进
* 使用4个空格代替tab，Pycharm会自动帮助缩进，也会自动将tab自动转换为4个空格。使用普通编辑器则严格使用4个空格缩进。
* 一些实例

```py
# 与起始变量对齐
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# 字典中与起始值对齐
d = {
    'k1': 'v1',
    'k2': 'v1',
    'k3': 'v1'
}
```


## 空行
* 顶级定义之间空两行，如类，函数定义。
* 方法定义之间空一行。
* 函数或方法中, 合适的地方空一行，有助于阅读代码逻辑。


## 空格
* 按照标准的排版规范来使用标点两边的空格
* 括号内不要有空格.
* 不要在逗号, 分号, 冒号前面加空格, 但应该在它们后面加(除了在行尾).
* 参数列表, 索引或切片的左括号前不应加空格.
* 在二元操作符两边都加上一个空格, 
  * 比如赋值(=), 比较(==, <, >, !=, <>, <=, >=, in, not in, is, is not), 
  * 布尔(and, or, not). 
  * 至于算术操作符两边的空格该如何使用, 需要你自己好好判断. 不过两侧务必要保持一致.
* 当'='用于指示关键字参数或默认参数值时, 不要在其两侧使用空格.
* 不要用空格来垂直对齐多行间的标记, 这会成为维护负担(适用于:, #, =等):
* 注释不需要添加多个空格来使每行注释都对齐。


## Shebang(#!)
* 大部分.py文件不必以#!作为文件的开始. 根据 [PEP-394](https://www.python.org/dev/peps/pep-0394/) 程序的main文件应该以 #!/usr/bin/python2或者 #!/usr/bin/python3开始.
* #!先用于帮助内核找到Python解释器, 但是在导入模块时, 将会被忽略. 因此只有被直接执行的文件中才有必要加入#!.


## 注释

### 文档字符串

* 三重双引号 `"""` [PEP-257](https://www.python.org/dev/peps/pep-0257/). 
* 是一行以句号/问号/惊叹号结尾的概述(或者该文档字符串单纯只有一行). 
* 接着是一个空行. 
* 接着是文档字符串剩下的部分, 它应该与文档字符串的第一行的第一个引号对齐. 

```py
def fun(v1, v2):
    """The doc string of fun.

    :param v1: parameter 1.
    :param v2: parameter 2.
    :return:
    """
    pass

```

### 模块
每个文件应该包含一个许可样板. 根据项目使用的许可(例如, Apache 2.0, BSD, LGPL, GPL), 选择合适的样板.

### 函数和方法
* 文档字符串应该包含函数做什么, 以及输入和输出的详细描述. 
* 通常, 不应该描述"怎么做", 除非是一些复杂的算法. 
* 文档字符串应该提供足够的信息, 当别人编写代码调用该函数时, 他不需要看一行代码, 只要看文档字符串就可以了. 
* 对于复杂的代码, 在代码旁边加注释会比使用文档字符串更有意义.
* 当写好函数定义后在def下一行输入六个双引号，Pycharm会自动将参数(param)以及return列出。

一个函数必须要有文档字符串, 除非它满足以下条件:
* 外部不可见
* 非常短小
* 简单明了

```py
def fetch_bigtable_rows(big_table, keys, other_silly_variable=None):
    """Fetches rows from a Bigtable.

    Retrieves rows pertaining to the given keys from the Table instance
    represented by big_table.  Silly things may happen if
    other_silly_variable is not None.

    :param big_table: An open Bigtable Table instance.
    :param keys: A sequence of strings representing the key of each table row to fetch.
    :param other_silly_variable: Another optional variable, that has a much longer name than the other args,
                and which does nothing.
    :return: A dict mapping keys to the corresponding table row data fetched.
            Each row is represented as a tuple of strings.
            For example:
                {'Serak': ('Rigel VII', 'Preparer'),
                 'Zim': ('Irk', 'Invader'),
                 'Lrrr': ('Omicron Persei 8', 'Emperor')}
    """
    pass

```

### 类
* 类应该在其定义下有一个用于描述该类的文档字符串. 
* 如果你的类有公共属性(Attributes), 那么文档中应该有一个属性(Attributes)段. 并且应该遵守和函数参数相同的格式.


```py
class SimpleClass(object):
    """Summary of class here.

    Longer class information....
    Longer class information....
    """

    def __init__(self, param):
        """ Initialization of SimpleClass.
        
        :param param: A boolean indicating if we like SPAM or not.
        :param key: An integer count of the eggs we have laid.
        """
        self.param = param
        self.key = 2

    def fun(self, param):
        """Have fun.

        :param param: A boolean indicating if we like SPAM or not.
        :return: xxx.
        """
        self.param = param * 10

```

### 块注释和行注释

* 最需要写注释的是代码中那些技巧性的部分. 
* 如果在下次代码审查的时候必须解释一下, 那么你应该现在就给它写注释. 
* 对于复杂的操作, 应该在其操作开始前写上若干行注释. 
* 对于不是一目了然的代码, 应在其行尾添加注释.
* 为了提高可读性, 注释应该至少离开代码2个空格.
* 不要描述代码. 假设阅读代码的人比你更懂Python, 他只是不知道你的代码要做什么.


## 类
* 如果一个类不继承自其它类, 就显式的从object继承. 嵌套类也一样.
* 继承自 `object` 是为了使属性(properties)正常工作, 并且这样可以保护你的代码, 使其不受Python 3000的一个特殊的潜在不兼容性影响. 
* 这样做也定义了一些特殊的方法, 这些方法实现了对象的默认语义, 包括 
    ```py
    __new__
    __init__
    __delattr__
    __getattribute__
    __setattr__
    __hash__
    __repr__
    __str__ 
    ```


## 字符串

* 连接字符串
  * 避免在循环中用+和+=操作符来累加字符串. 字符串是不可变的, 这会创建不必要的临时对象, 并导致二次方的运行时间. 
  * 作为替代方案, 你可以将每个子串加入列表, 然后在循环结束后用 .join 连接列表.
    ```py
    shown_items = ('count', 'include', 'item_ID', 'bible_classification', 'conf_mm', 'conf_desc', None)
    shown_string = "; ".join([str(item) for item in shown_items if item])
    print(shown_string)
    'count; include; item_ID; bible_classification; conf_mm; conf_desc'
    ```
* 在同一个文件中, 保持使用字符串引号的一致性. 使用单引号'或者双引号"之一用以引用字符串, 并在同一文件中沿用. 在字符串内可以使用另外一种引号, 以避免在字符串中使用. PyLint已经加入了这一检查.
* 为多行字符串使用三重双引号"""而非三重单引号'''. 
* 当且仅当项目中使用单引号'来引用字符串时, 才可能会使用三重'''为非文档字符串的多行字符串来标识引用. 
* 文档字符串必须使用三重双引号""". 不过要注意, 通常用隐式行连接更清晰, 因为多行字符串与程序其他部分的缩进方式不一致.
* Python 3.6 及以后版本中都加入在字符串中替换变量的方法。
  * 在字符串前加上f，然后字符串中用大括号括起来变量名。
  * 最终变量的值就会被替换到字符串中，这样会使代码变得更为简洁和直观。
  * 大括号中还可以使用格式控制，其参数与format是一样的。
  * 一个例子：
    ```py
    name = 'Miles'
    s = f'This sentenst contains {name}'
    print(s)
    This sentenst contains Miles
    ```


## 文件和sockets
* 如果是显式的打开文件/sockets时，在结束时请显式的关闭它.
* 推荐使用 `with` 打开或关闭文件/socket，因为with语句会在代码执行完成之后自动将文件/socket关闭。


## TODO注释

```py
# TODO(jjohnson2): Provide OEM extensibility to cover user deletion
```

* TODO注释
  * 在所有开头处包含"TODO"字符串, 
  * 紧跟着是用括号括起来的你的名字/email/其它标识符. 
  * 然后是一个可选的冒号. 
  * 接着必须有一行注释, 解释要做什么. 主要目的是为了有一个统一的TODO格式, 这样添加注释的人就可以搜索到(并可以按需提供更多细节). 
* 写了TODO注释并不保证写的人会亲自解决问题. 当你写了一个TODO, 请注上你的名字.
* 如果你的TODO是"将来做某事"的形式, 那么请确保你包含了一个指定的日期("2009年11月解决")或者一个特定的事件("等到所有的客户都可以处理XML请求就移除这些代码").


## 导入格式
```py
import os
import sys

from redfishtool import main
```

* 每个导入应该独占一行
* 导入总应该放在文件顶部, 位于模块注释和文档字符串之后, 模块全局变量和常量之前. 导入应该按照从最通用到最不通用的顺序分组:
  * 标准库导入
  * 第三方库导入
  * 应用程序指定导入
* 每种分组中, 应该根据每个模块的完整包路径按字典序排序, 忽略大小写


## 语句
* 每个语句应该独占一行


## 访问控制
* 对于琐碎又不太重要的访问函数, 你应该直接使用公有变量来取代它们, 这样可以避免额外的函数调用开销. 当添加更多功能时, 你可以用属性(property)来保持语法的一致性.
* 如果访问更复杂, 或者变量的访问开销很显著, 那么你应该使用像 get_foo() 和 set_foo() 这样的函数调用. 
* 如果之前的代码行为允许通过属性(property)访问 , 那么就不要将新的访问函数与属性绑定.


## 命名

### 应该避免的名称
* 单字符名称, 除了计数器和迭代器.
* 包/模块名中的连字符(-)
* 双下划线开头并结尾的名称(Python保留, 例如__init__)

### 命名约定

* 所谓"内部(Internal)"表示仅模块内可用, 或者, 在类内是保护或私有的.
* 用单下划线(_)开头表示模块变量或函数是protected的(使用import * from时不会包含).
* 用双下划线(__)开头的实例变量或方法表示类内私有.
* 将相关的类和顶级函数放在同一个模块里. 不像Java, 没必要限制一个类一个模块.
* 对类名使用大写字母开头的单词(如CapWords, 即Pascal风格), 但是模块名应该用小写加下划线的方式(如lower_with_under.py). 尽管已经有很多现存的模块使用类似于CapWords.py这样的命名, 但现在已经不鼓励这样做, 因为如果模块名碰巧和类名一致, 这会让人困扰.

**Python之父Guido推荐的类/方法/函数/变量的命名规范**

Type	|   Public	|   Internal
--------|-----------|-----------------------
Modules	|   lower_with_under	|   _lower_with_under
Packages	|   lower_with_under	|    
Classes	|   CapWords	|   _CapWords
Exceptions	|   CapWords	|    
Functions	|   lower_with_under()	|   _lower_with_under()
Global/Class Constants	|   CAPS_WITH_UNDER	|   _CAPS_WITH_UNDER
Global/Class Variables	|   lower_with_under	|   _lower_with_under
Instance Variables	|   lower_with_under	|   _lower_with_under (protected) or __lower_with_under (private)
Method Names	|   lower_with_under()	|   _lower_with_under() (protected) or __lower_with_under() (private)
Function/Method Parameters	|   lower_with_under	|    
Local Variables	|   lower_with_under	|    


## Main

* 即使是一个打算被用作脚本的文件, 也应该是可导入的. 并且简单的导入不应该导致这个脚本的主功能(main functionality)被执行, 这是一种副作用. 主功能应该放在一个main()函数中.
* 在Python中, pydoc以及单元测试要求模块必须是可导入的. 你的代码应该在执行主程序前总是检查 `if __name__ == '__main__':` 这样当模块被导入时主程序就不会被执行.
* 所有的顶级代码在模块导入时都会被执行. 要小心不要去调用函数, 创建对象, 或者执行那些不应该在使用pydoc时执行的操作.








## reference
* [Python 编码规范(Google)](http://www.runoob.com/w3cnote/google-python-styleguide.html)



