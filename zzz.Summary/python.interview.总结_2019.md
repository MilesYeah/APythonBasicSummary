# python面试题总结_2019




## python特性






### 1 谈谈对 Python 和其他语言的区别
略






### 2 简述解释型和编译型编程语言
编译型语言：把做好的源程序全部编译成二进制代码的可运行程序。然后，可直接运行这个程序。


解释型语言：把做好的源程序翻译一句，然后执行一句，直至结束。






### 3 Python 的解释器种类以及相关特点？
CPython


　　由C语言开发的  使用最广的解释器


IPython


　　基于cpython之上的一个交互式计时器 交互方式增强 功能和cpython一样


PyPy


　　目标是执行效率 采用JIT技术 对python代码进行动态编译，提高执行效率


JPython


　　运行在Java上的解释器 直接把python代码编译成Java字节码执行


IronPython


　　在微软 .NET 平台上的解释器，把python编译成. NET 的字节码






### 4 说说你知道的Python3 和 Python2 之间的区别
1. 是print的区别。python2中print是语句，要显示的对象不需要括号；python3中print是函数，要显示的对象需要加上括号。如：python2中的print 'A=',5。在python3中改为print('A=',5)
2. 是字符串存储的区别。python2中 字符串以 8-bit 字符串存储，python3中字符串以 16-bit Unicode 字符串存储。存储格式得到了升级
3. 是除法的区别。python2中 10/3=3，python3中改为10/3=3.3333333333333335，更精确啦，而10//3=3，这个//才是取整运算符。除法有了多样性选择
4. 是纠错机制的区别。python2 中try:...except Exception, e :...，改为python3中的 try:...except Exception as e :...。加了个as使代码更清晰啦
5. 在 Python 2 中 xrange() 创建迭代对象的用法是非常流行的，在 Python 3 中，range() 是像 xrange() 那样实现以至于一个专门的 xrange() 函数都不再存在（在 Python 3 中 xrange() 会抛出命名异常）。range与xrange的区别是：
   1. （1）range，函数说明：range([start,]stop[,step]),根据start和stop的范围以及步长step生成一个序列
   2. （2）xrange，函数说明：功能和range一样，所不同的是生成的不是一个数组而是一个生成器
   3. （3）主要区别：xrange比range的性能和效率更优，
      1. 所以，在Range的方法中，它会生成一个list的对象，但是在XRange中，它生成的却是一个xrange的对象。
      2. 当返回的东西不是很大的时候，或者在一个循环里，基本上都是从头查到底的情况下，这两个方法的效率差不多。
      3. 但是，当返回的东西很大，或者循环中常常会被Break出来的话，还是建议使用XRange，这样既省空间，又会提高效率。
6. 八进制数必须写成0o777，原来的形式0777不能用了；二进制必须写成0b111。新增了一个bin()函数用于将一个整数转换成二进制字串。 Python 2.6已经支持这两种语法。在Python 3.x中，表示八进制字面量的方式只有一种，就是0o1000。
7. Python 2.x中不等于有两种写法 != 和 <>  Python 3.x中去掉了<>, 只有!=一种写法，还好，我从来没有使用<>的习惯
8. Py3.X去除了long类型，现在只有一种整型——int，但它的行为就像2.X版本的long 2）新增了bytes类型，对应于2.X版本的八位串
9.  是打开文件的区别。python2中用file(.....)或者open(……)来打开文件，改为python3中只能用open(.....)来打开文件。更符合python之禅中简单明了无歧义的要求
10. 是键盘输入的区别。从键盘录入一个字符串，python2中是 raw_input( "提示信息" )，python3中是 input( "提示信息" )。让代码更简洁啦
11. 是库的变化。
    1.  python2中的urllib、urilib2两个库合并为python3中的urllib库；
    2.  python2中的urllib2.urlopen()变为python3中的urllib.request.urlopen()；
    3.  python2中的urllib2.Request()变为python3中的urllib.request.Request()；
    4.  python2中的urllib.quote(text)变为python3中的urllib.parse.quote(text)；
    5.  python2中的urllib.urlencode 变为python3中的urllib.parse.urlencode；
    6.  python2中的urllib2 变为python3中的urllib.request；
    7.  python2中的urlparse 变为python3中的 urllib.parse；
    8.  python2中的cStringIO变为python3中的io
以上的区别都描述的比较具体，便于理解记忆，网上也有更抽象更全面的描述，这里没有引用；






### 5 Python3 和 Python2 中 int 和 long 区别？
如果32位的编译系统，两者都是4字节，即32bits，如果是64位的编译系统，int是4字节，long是8字节






### 6 xrange 和 range 的区别
5. 在 Python 2 中 xrange() 创建迭代对象的用法是非常流行的，在 Python 3 中，range() 是像 xrange() 那样实现以至于一个专门的 xrange() 函数都不再存在（在 Python 3 中 xrange() 会抛出命名异常）。range与xrange的区别是：
   1. （1）range，函数说明：range([start,]stop[,step]),根据start和stop的范围以及步长step生成一个序列
   2. （2）xrange，函数说明：功能和range一样，所不同的是生成的不是一个数组而是一个生成器
   3. （3）主要区别：xrange比range的性能和效率更优，
      1. 所以，在Range的方法中，它会生成一个list的对象，但是在XRange中，它生成的却是一个xrange的对象。
      2. 当返回的东西不是很大的时候，或者在一个循环里，基本上都是从头查到底的情况下，这两个方法的效率差不多。
      3. 但是，当返回的东西很大，或者循环中常常会被Break出来的话，还是建议使用XRange，这样既省空间，又会提高效率。





## 编码规范


### 7 什么是 PEP8?
PEP8是一个编程规范，内容是一些关于如何让你的程序更具可读性的建议






### 8 了解 Python 之禅么？
打开界面 import this 可显示






### 9 了解 dosctring 么？
三重引号中的信息






### 10 了解类型注解么？
用 : 类型 的形式指定函数的 参数类型 ，用 -> 类型 的形式指定函数的 返回值 类型

```py
def add(x, y):
    return x + y
```

可以写成：

```py
def add(x:int, y:int) -> int:
    return x + y
```

这样对于函数读者，可以快速知道输入输出的数据类型；






### 11 例举你知道 Python 对象的命名规范，例如方法或者类等
如无特殊情况, 文件一律使用 UTF-8 编码 
如无特殊情况, 文件头部必须加入#--coding:utf-8--标识


统一使用 4 个空格进行缩进 
每行代码尽量不超过 80 个字符(在特殊情况下可以略微超过 80 ，但最长不得超过 120) 理由： 这在查看 side-by-side 的 diff 时很有帮助 方便在控制台下查看代码 太长可能是设计有缺陷


简单说，自然语言使用双引号，机器标示使用单引号，因此 代码里 多数应该使用 单引号 
自然语言 使用双引号 "…" 例如错误信息；很多情况还是 unicode，使用u"你好世界" 
机器标识 使用单引号 '…' 例如 dict 里的 key 正则表达式 使用原生的双引号 r"…" 
文档字符串 (docstring) 使用三个双引号 """……"""






### 12 Python 中的注释有几种？
单行注释符号,#

多行注释符号,3对单引号''' '''或者3对双引号""" """






### 13 如何优雅的给一个函数加注释？
同10，函数注释也就是类型注解






### 14 如何给变量加注释？
直接加#好了






### 15 Python 代码缩进中是否支持 Tab 键和空格混用。
不支持，但是notpad++，首选项/语言中可以将TAP替换为空格，对于python文件来说只存在空格即使在编辑的时候你用了tap，这样就不怕python报错了；






### 16 是否可以在一句 import 中导入多个库?
可以，建议每次一个






### 17在给 Py 文件命名的时候需要注意什么?
有意义






### 18 例举几个规范 Python 代码风格的工具
pylint




### 19 列举 Python 中的基本数据类型？
int, bool, str, list, tuple, dict, set






### 20 如何区别可变数据类型和不可变数据类型
不可变数据类型： 当该数据类型的对应变量的值发生了改变，那么它对应的内存地址也会发生改变，对于这种数据类型，就称不可变数据类型。


可变数据类型    ：当该数据类型的对应变量的值发生了改变，那么它对应的内存地址不发生改变，对于这种数据类型，就称可变数据类型。


总结：不可变数据类型更改后地址发生改变，可变数据类型更改地址不发生改变


不可变数据类型: int, str, tuple


可变数据类型：set, list, dict







## 基本语法

### 21 将"hello world"转换为首字母大写"Hello World"
```py
name = "hell world"
name_1 = name.capitable()
```





### 22 如何检测字符串中只含有数字?
```py
print("1234".isnumeric())
```





### 23 将字符串"ilovechina"进行反转
1. 使用字符串切片 result = s[::-1]
2. result = "ilovechina".reverse()
3. 使用出栈,pop
4. for循环或者递归函数




### 24 Python 中的字符串格式化方式你知道哪些？
(1)用%实现，%s字符串, %d整数, %f浮点数，平时print常用


(2) 格式化字符串的函数 str.format()


格式化字符串的函数 str.format()，它增强了字符串格式化的功能。str中包含占位符，text中是要填充的内容


基本语法是通过 {} 和 : 来代替以前的 % 。


优点：format 函数可以接受不限个参数，位置可以不按顺序。


使用'{}'占位符


使用'{0}','{1}'形式的占位符


使用'{name}'形式的占位符


example：使用'{name} # 设置指定位置


info= '亲爱的{user}你好！你{month}月的花费是{huafei}，余额是{balance}'


info = info.format(user='xiaoming',month=10,huafei=50.0,balance=29.29)


print info


example：使用'{0}','{1}'形式的占位符：# 设置指定位置


info1= '亲爱的{0}你好！你{1}月的花费是{2}，余额是{3}'


info1 = info1.format('xiaoming',2,50.0,29.29)


print info1


example：使用{}占位符：# 不设置指定位置，按默认顺序


a = "{} {}".format("hello", "world")


print a






### 25 有一个字符串开头和末尾都有空格，比如" adabdw ",要求写一个函数把这个字符串的前后空格都去掉
* strip()：把头和尾的空格去掉，lstrip()：把左边的空格去掉，rstrip()：把右边的空格去掉
* eplace('c1','c2'):把字符串中的c1替换成c2，用(' ',')去掉空格
* plit():对字符串用空格切片




### 26 获取字符串"123456"最后的两个字符。
```py
result = "123456"[-2:]
```





### 27 怎样将字符串s转换为小写？

* capitalize() # 首字母大写，其余全部小写
* upper() # 全转换成大写
* lower() # 全转换成小写

将字符串转成小写操作：result = s.lower()






### 28 单引号、双引号、三引号的区别？

单引号中需要转义，双引号，三引号不需要转义；


三引号可以包含双引号、单引号，双引号可以包含单引号；


三引号可以多行写，单引号双引号需要换行符\






### 29 a = "你好     中国  ",去除多余空格只留一个空格。
```py
result = ' '.join(a.split())
```





### 30 已知 AList = [1,2,3,1,2],对 AList 列表元素去重，写出具体过程
(1)for循环

```py
result = []
for i in range(len(AList)):
       if AList[i] not in result:
              result.append(AList[i])
print(result)
```

(2)用set和sort方法

```py
new_s = list(set(AList)) 
new_s.sort(key= AList.index)
```

(3) fromkeys生成一个字典，keys返回字典的键值，这里利用了键值不能重复的性质

```py
result = a.fromkeys(s).keys()
```

(4)reduce方法

```py
result = reduce(lambda x,y:x if y in x else x + [y], [[],] + s)
```





### 31 如何实现 "1,2,3" 变成 ["1","2","3"]
```py
result = list("1,2,3".split(','))
```





### 32 给定两个 list，A 和 B，找出相同元素和不同元素
(1)for循环直接实现

```py
same =[]
usame= []
for i in a:
    if i in b:
        same.append(i)
    else:
        usame.append(i)
for i in b：
    if I not in a:
        usame.append(i)
```

(2)set实现: set() 函数创建一个无序不重复元素集，称为集合，是数据类型的一种，有集合的性质,可进行关系测试，删除重复数据，还可以计算交集(&)、差集(-)、并集(|)等

```py
same = set(a)&set(b)
usame = set(a)^set(b)
```





### 33 [[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
```py
import numpy as np
result = np.arange([[1,2],[3,4],[5,6]]).flatten()
```





### 34 合并列表[1,5,7,9]和[2,2,6,8]
```py
a = [1,5,7,9]
b = [2,2,6,8]
```

1. result = a + b
2. a+=b
3. a.extend(b)

这里不能用append，list.append(object) 向列表中添加一个对象object，list.extend(sequence) 把一个序列seq的内容添加到列表中，


a.append(b)后是这样的[1,5,7,9,[2,2,6,8]]






### 35 如何打乱一个列表的元素？
```py
from ramdom import shuffle
shuffle(mylist)
```









## 字典操作


### 36 字典操作中 del 和 pop 有什么区别

* remove是根据元素删除；
* del是根据索引删除；也可以根据索引删除指定范围的值，del a[1,4]，del a表示删除整个列表；
* pop()会弹出列表末尾的元素，也可以通过索引的方式删除列表指定的元素；




### 37按照字典的内的年龄排序
```py
dict01 = [{'name':'alice', 'age':38},
    {'name':'bob', 'age':18},
    {'name':'Carl', 'age':28},]
```

首先明确dict01不是dict而是list数据类型；


(1)

```py
import operator
result = sorted(dict01, key=operator.itemgetter('age'), reverse = 'False')
```

(2)

```py
result = sorted(dict01, key=lambda dict01:dict01['age'])
```

注：因为用word编辑的原因，本文的所有的单双引号应该是不能直接移植运行程序，请注意修改再运行






### 38 请合并下面两个字典 a = {"A":1,"B":2},b = {"C":3,"D":4}
```py
dict(a, **b)
dict(**a, **b)
result = a.copy()  

z.update(y)
```





### 39 如何使用生成式的方式生成一个字典，写一段功能代码
创建字典还是改写字典？


创建字典：

```py
dict0 = {}
dict1 = {'data':1, 'weight':2, 'bias':3}
dict2 = dict(data = 1,weight = 2, bias = 3)
dict3 = dict(zip(['data','weight','bias'],[1,2,3]))
```

按照要求修改字典(例如key修改成大写，value不变)：

```py
dict4 = ({k.upper():v for k, v in dict2.items()})
```





### 40 如何把元组("a","b")和元组(1,2)，变为字典{"a":1,"b":2}
见39，dict3方法






## 综合特性


### 41 Python 常用的数据结构的类型及其特性？
与19略重复


python中常见的数据结构有元组（tuple）、列表（list）、字典（dic）、集合（set）


1、元组用小括号表示（）


2、列表用中括号表示 [ ]


3、字典用大括号表示 { }


4、集合用关键字set（）来表示


5、字符串用"  "或者'  '表示


6、数值型数据直接用本身表示即可，不需要添加任何修饰


相互之间的区别和特点为元组和字典中的键、字符串、整型和浮点型为不可变类型，也就是说不能对其进行修改；而列表和集合为可变类型，可以直接对其进行修改。同时因为列表和集合为可变类型，因此不能作为字典中的键。






### 42 如何将元组("A","B")和元组(1,2),合并成字典{"A":1,"B":2}
见40






### 43 Python 里面如何实现 tuple 和 list 的转换？
result = list(tuple)


result = tuple(list)






### 44 我们知道对于列表可以使用切片操作进行部分元素的选择，那么如何对生成器类型的对象实现相同的功能呢？
生成器是特殊的迭代器，使用了yield的迭代器就叫生成器


(1)
```py
import itertools

def count(n):
    while True:
        yield n
        n+=1

result = count(0)

for r in itertools.islice(result,5,10):
    print(r)
```
(2)
```py
import itertools

generator_1 = (x*2 for x in range(10))

for i in itertools.islice(generator_1,5,8):
    print(i)
```




### 45 请将[i for i in range(3)]改成生成器
result = (i for i in range(3))






### 46 a="hello"和 b="你好"编码成 bytes 类型
```py
result_01 = a.encode('utf-8')
result_02 = b.encode('uft-8')
```

result_02的显示是一串字符，如果想再显示成'你好'可以result_02.encode('utf-8')






### 47 下面的代码输出结果是什么？
```py
a = (1,2,3,[4,5,6,7],8)
a[2] = 2
```

结果：TypeError: 'tuple' object does not support item assignment






### 48 下面的代码输出的结果是什么?
```py
a = (1,2,3,[4,5,6,7],8)
a[5] = 2
```

结果：TypeError: 'tuple' object does not support item assignment






### 49 li = [lambda :x for x in range(10)] li中元素是什么类型？
```py
print(type(li))
print(type(li[0]))
<class 'list'>
<class 'function'>
```












## 操作类




### 50 Python 交换两个变量的值
(1) temp做中间量

```py
temp = a
a = b
a = temp
```

(2) `a,b = b,a`


### 51 在读文件操作的时候会使用 read、readline 或者 readlines，简述它们各自的作用
read 读取整个文件


readline 读取下一行，for循环中经常用


readlines 读取整个文件到一个迭代器，for中也可以


### 52 json序列化时，可以处理的数据类型有哪些？如何定制支持 datetime 类型？
(1) 可以处理的数据类型是 string、int、list、tuple、dict、bool、null


json.dumps()   将Python中的对象转换为JSON中的字符串对象
json.loads()   将JSON中的字符串对象转换为Python中的对象


(2) 自定义时间序列化转换器
```py
import json
from json import JSONEncoder
from datetime import datetime
class ComplexEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return super(ComplexEncoder,self).default(obj)
d = { 'name':'alex','data':datetime.now()}
print(json.dumps(d,cls=ComplexEncoder))
# {"name": "alex", "data": "2018-05-18 19:52:05"}
```


### 53 json 序列化时，默认遇到中文会转换成 unicode，如果想要保留中文怎么办？
```py
import json
a=json.dumps({"ddf":"你好"},ensure_ascii=False)
print(a) #{"ddf": "你好"}
```





### 54 有两个磁盘文件 A 和 B，各存放一行字母，要求把这两个文件中的信息合并，输出到一个新文件 C 中


(1)
```py
import os
import shutil
outfile = open('C','w')
infile1 = open('A','r')
infile2 = open('B','r')
shutil.copyfileobj(infile1,outfile)
outfile.write('\n')
shutil.copyfileobj(infile2,outfile)
infile1.close()
infile2.close()
outfile.close()
```
(2)
```py
import os
import shutil
with open('C','w') as c, open('A','r') as a, open('B','r') as b:
    shutil.copyfileobj(a,c)
    shutil.copyfileobj(b,c)
```






### 55 如果当前的日期为 20190530，要求写一个函数输出 N 天后的日期，(比如 N 为 2，则输出 20190601)。
```py
import datetime


def getday(n):
    y = 2019
    m = 5
    d = 30
    #datetime.datetime指定日期
    the_date = datetime.datetime(y,m,d)
    #datetime.timedelta,时间差
    result_date = the_date + datetime.timedelta(days = n)
    target_date = result_date.strftime('%Y%m%d')
    return target_date


print(getday(2))
```


### 56 写一个函数，接收整数参数 n，返回一个函数，函数的功能是把函数的参数和 n 相乘并把结果返回。
(1)这种形式的函数称为闭包
```py
def func01(n):
    def func02(m):
        return n * m
    return func02
zw = func01(7)
print(zw(9))
```


### 57 下面代码会存在什么问题，如何改进？
```py
def strappend(num):
    str='first'
    for i in range(num):
        str+=str(i)
    return str
```
该错误TypeError: 'str' object is not callable字面上意思:就是str不可以被系统调用,其实原因就是:你正在调用一个不能被调用的变量或对象，具体表现就是你调用函数、变量的方式错误.


将str(i)修改成str[i]


### 58一行代码输出 1-100 之间的所有偶数
(1) print([i*2 for i in range(1,51)])


(2) print(list(x for x in range(1,101) if x%2==0))


或者 print([x for x in range(1,101) if x%2==0])


关于加list或者[]这里解释一下，如果不加运行的话会出现`<generator object <genexpr> at 0x0000000002945360>`这里的意思是生成了一个迭代器(python generator object)对象，加list或者[]则创建了一个list对象，因此这样才可以打印出想要的数据


### 59 with 语句的作用，写一段代码？
with语句使用于对资源进行访问的场合。确保使用过程中不管是否发生异常，都会执行必要的"清理"操作，并释放资源。比如文件使用后自动关闭，线程中锁的自动获取和释放。


见53(2)


### 60 python字典 和 json字符串相互转化方法
json.dumps()   将Python中的对象转换为JSON中的字符串对象
json.loads()   将JSON中的字符串对象转换为Python中的对象


上述函数对字典使用


### 61请写一个 Python 逻辑，计算一个文件中的大写字母数量
(1)
```py
import os

with open('file_name') as file:
    count = 0
    file_o = file.read()
    for i in file_o:
        if i.isupper():
            count +=1

print(count)
```
(2)
```py
import re

with open('file_name') as file:
    file_o = file.read()
    len_capital = len(re.compile(r'[A-Z]').findall(file_o))

print(len_capital)
```




## python的进阶问题


### 62 函数装饰器有什么作用？请列举说明？
当程序使用"＠函数"（比如函数 A）装饰另一个函数（比如函数 B）时，实际上完成如下两步
* 将被修饰的函数（函数 B）作为参数传给＠符号引用的函数（函数 A）。
* 将函数B替换（装饰）成第 1 步的返回值。


例如：
```py
def funA(fn):
    print('A')
    fn() # 执行传入的fn参数
    return 'end'


@funA
def funB():
    print('B')
    print(funB) # end
```


上面程序的执行结果是
```py
A
B
end
```
修改函数funA后会在执行print(funB)时，先返回修改的函数funA(),则会打印A，fn()执行传入的funB(),则会打印B，然后打印返回的参数end




### 63 Python 垃圾回收机制？
主要以引用计数为主，分代回收为辅


详细来说是一个比较麻烦的问题，链接如下：


https://blog.csdn.net/xiongchengluo1129/article/details/80462651






### 64魔法函数 __call__怎么使用?
所谓的魔法方法就是增加一些特殊功能，__call__就是使不可调用对象可以被调用


函数可以被调用，但是类不可以被调用，例如
```py
class test():
  def method(self):
    return 1


a = test()
```
callable(a)是flase，这种情况修改成：
```py
class test():
  def __call__(self):
    return 1


a = test()
```
callable(a)是true


目前还有个疑惑的地方，可不可调用只是通过callable验证的，其实print(a.method())和print(a.__call__())都可以输出1，所以是否可调用有什么用呢？


### 65如何判断一个对象是函数还是方法？
#### 首先，从分类的角度来分析。


（1）函数的分类：
* 内置函数：python内嵌的一些函数。
* 匿名函数：一行代码实现一个函数功能。
* 递归函数：
* 自定义函数：根据自己的需求，来进行定义函数。


（2）方法的分类：
* 普通方法：直接用self调用的方法。
* 私有方法：__函数名，只能在类中被调用的方法。
* 属性方法：@property，将方法伪装成为属性，让代码看起来更合理。
* 特殊方法(双下划线方法)：以__init__为例，是用来封装实例化对象的属性，只要是实例化对象就一定会执行__init方法，如果对象子类中没有则会寻找父类（超类），如果父类（超类）也没有，则直接继承object（python 3.x）类，执行类中的__init__方法。
* 类方法：通过类名的调用去操作公共模板中的属性和方法。
* 静态方法：不用传入类空间、对象的方法， 作用是保证代码的一致性，规范性，可以完全独立类外的一个方法，但是为了代码的一致性统一的放到某个模块（py文件）中

#### 其次，从作用域的角度来分析：


* （1）函数作用域：从函数调用开始至函数执行完成，返回给调用者后，在执行过程中开辟的空间会自动释放，也就是说函数执行完成后，函数体内部通过赋值等方式修改变量的值不会保留，会随着返回给调用者后，开辟的空间会自动释放。
* （2）方法作用域：通过实例化的对象进行方法的调用，调用后开辟的空间不会释放，也就是说调用方法中对变量的修改值会一直保留。


#### 最后，调用的方式不同。


* (1) 函数：通过"函数名( )"的方式进行调用。
* (2) 方法：通过"对象.方法名"的方式进行调用。
```py
class Foo(object):


    def func(self):


        pass
```
实例化
```py
obj = Foo()
```
执行方式一:调用的func是方法
```py
obj.func() #func 方法
```
执行方式二：调用的func是函数
```py
Foo.func(123) # 函数
```
检测是函数还是方法可以通过内置的isinstance来判断：
```py
from types import MethodType, FunctionType
print(isinstance(obj.func, MethodType)) #true
print(isinstance(Foo.func, FunctionType)) #true
```




### 66 @classmethod 和@staticmethod 用法和区别
Python中3种方式定义类方法, 常规方式, @classmethod修饰方式, @staticmethod修饰方式，例如：
```py
class A(object):
    def foo(self, x):
        print("executing foo(%s,%s)" % (self, x))
        print('self:', self)


    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s,%s)" % (cls, x))
        print('cls:', cls)
        cls.foo('hello') #这是@classmethod与@staticmethod的区别


    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)
        a = A()
```
普通的类方法foo()需要通过self参数隐式的传递当前类对象的实例。 @classmethod修饰的方法class_foo()需要通过cls参数传递当前类对象。@staticmethod修饰的方法定义与普通函数是一样的。


self和cls的区别不是强制的，只是PEP8中一种编程风格，slef通常用作实例方法的第一参数，cls通常用作类方法的第一参数。即通常用self来传递当前类对象的实例，cls传递当前类对象。


要使用某个类的方法，需要先实例化一个对象再调用方法。而使用@staticmethod或@classmethod，就可以不需要实例化，直接类名.方法名()来调用，如下：


foo可通过实例a调用，通过类对象调用(A.foo(1))会出错


a.foo(1)


class_foo通过类对象或者对象实例调用


static_foo通过类对象或者对象实例调用


@staticmethod和@classmethod的区别是有两点：


从它们的使用上来看,


@staticmethod不需要表示自身对象的self和自身类的cls参数，就跟使用函数一样。


@classmethod也不需要self参数，但第一个参数需要是表示自身类的cls参数。


如果在@staticmethod中要调用到这个类的一些属性方法，只能直接`类名.属性名`或`类名.方法名`。而@classmethod因为持有cls参数，可以来调用类的属性，类的方法，实例化对象等，避免硬编码。








### 67 Python 中的接口如何实现？
https://blog.csdn.net/weixin_41762173/article/details/82783723


简单来说，域名（地址）带上参数就是一个接口，然后通过调用此接口就可获取这个地址下的参数了，如：<https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=ACCESS_TOKEN > 就是一个接口，
？后面的就是接口携带的常量参数，此接口会携带一个或多个返回值。
```py
{"errcode":40014,"errmsg":"invalid access_token"}
```




### 68 Python 中的反射了解么?
https://www.cnblogs.com/benric/p/5069205.html


https://www.cnblogs.com/iexperience/p/9206485.html


1. 有时我们要访问某个变量或是方法时并不知道到底有没有这个变量或方法，所以就要做些判断。判断是否存在字符串对应的变量及方法。
2. 我们知道访问变量时是不能加引号的，否则会被当成字符串处理。如果要通过字符串找到对应的变量，那该怎么办呢

反射就是用于解决上面两个问题而产生的，所谓反射，按我的理解就是反过来告诉我字符串是什么，是变量or方法




### 69 metaclass 作用？以及应用场景？

metaclass的实例化结果是类，而class实例化的结果是instance。

metaclass，直译为元类，简单的解释就是：

当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。

但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。

连接起来就是：先定义metaclass，就可以创建类，最后创建实例。

所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的"实例"。






### 70 hasattr() getattr() setattr()的用法
见76








### 71 请列举你知道的 Python 的魔法方法及用途。
魔法方法还是挺多的，参考下面链接：


https://blog.csdn.net/koko66/article/details/42709279








### 72如何知道一个 Python 对象的类型？
print(type(object))












### 73Python 的传参是传值还是传址？
Python是不允许程序员选择采用传值还是传址的。Python参数传递采用的肯定是"传对象引用"的方式。实际上，这种方式相当于传值和传址的一种综合。


如果函数收到的是一个可变对象（比如字典或者列表）的引用，就能修改对象的原始值——相当于传址。如果函数收到的是一个不可变对象（比如数字、字符或者元组）的引用（其实也是对象地址！！！），就不能直接修改原始对象——相当于传值。


所以python的传值和传址是比如根据传入参数的类型来选择的


https://blog.csdn.net/github_39261590/article/details/74002290










### 74Python中的元类(metaclass)使用举例
见77










### 75简述any()和all()方法
any(x)判断x对象是否为空对象，如果都为空、0、False，则返回False，如果不都为空、0、False，则返回True


all(x)如果all(x)参数x对象的所有元素不为0、''、False或者x为空对象，则返回True，否则返回False










### 76filter方法求出列表所有奇数并构造新列表，a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
(1)
```py
a = [1,2,3,4,5,6,7,8,9,10]

def fn(a):
    return a%2==1

newlist = filter(fn,a)
newlist = [i for i in newlist]
print(newlist)
```
(2)
```py
a = [1,2,3,4,5,6,7,8,9,10]
res = [i for i in a if i%2==1]
print(res)
```


关于为什么在(1)中有newlist = [i for i in newlist]这一句，或者(2)中res = [i for i in a if i%2==1]


用中括号，解释见57
```py
>>> list(filter(lambda x:x%2!=0, a))
[1, 3, 5, 7, 9]
```


### 77什么是猴子补丁？
monkey patch指的是在执行时动态替换,通常是在startup的时候.用过gevent就会知道,会在最开头的地方gevent.monkey.patch_all();把标准库中的thread/socket等给替换掉.
这样我们在后面使用socket的时候能够跟寻常一样使用,无需改动不论什么代码,可是它变成非堵塞的了.

之前做的一个游戏server,非常多地方用的import json,后来发现ujson比自带json快了N倍,于是问题来了,难道几十个文件要一个个把import json改成import ujson as json吗?
事实上仅仅须要在进程startup的地方monkey patch即可了.是影响整个进程空间的.

同一进程空间中一个module仅仅会被执行一次










### 78在 Python 中是如何管理内存的？
内存分配方式有四种:


1. 从静态存储区域分配。内存在程序编译的时候就已经分配好，存放全局变量和静态变量，这些内存在程序运行期间都存在。
2. 在栈上创建。由编译器自动分配自动释放，用于存放局部变量和参数，栈内的对象先进后出，所以先创建的对象会后析构。栈由于是编译器自动管理的，所以栈内的对象不会存在内存泄露问题，并且效率很高，但是分配的内存容量有限。
3. 从堆上分配，亦称动态内存分配。程序员自己负责在何时用free或delete释放内存。动态内存的生存期由我们决定，使用非常灵活，但问题也最多。
4. 常量区：存放常量字符串，程序结束后由系统释放

python的内存管理是由私有的heap空间管理的，所有的python对象和数据结构都在一个专有的heap（堆），程序员没有访问该heap的权限，只有解释器才能对他进行操作。
而python的heap空间分配是由内存管理模块进行的，其核心API会提供一些访问该模块的方法提供程序员使用。


python自带的垃圾回收系统，它会回收并释放没有被使用的内存，让她们能够被其他程序使用（内存池。被释放后先回到内存池然后再被别的程序所运用）














### 79当退出 Python 时是否释放所有内存分配？
循环引用其他对象或引用自全局命名空间的对象的模块，在python退出时并非完全释放


另外，也不会释放c库保留的内存部分












## 正则表达式


说明下r的作用，加上r表示原生字符串，如果没有r需要表示\则需要4个\才可以，具体情况看以下示例：
```py
>>> mm = "c:\\a\\b\\c"
>>> mm
'c:\\a\\b\\c'
>>> print(mm)
c:\a\b\c
>>> re.match("c:\\\\",mm).group()
'c:\\'
>>> ret = re.match("c:\\\\",mm).group()
>>> print(ret)
c:\
>>> ret = re.match("c:\\\\a",mm).group()
>>> print(ret)
c:\a
>>> ret = re.match(r"c:\\a",mm).group()
>>> print(ret)
c:\a
```
再说一个( )与[ ]的区别：


( )内是以字符串形式匹配的，例如(abs)则是匹配abs整个字符串，(abs|asb)则是匹配abs或者asb，
[ ]内部是以单个字符进行匹配，[a-z]则是匹配a到z的任意一个字符








### 80 使用正则表达式匹配出<html><h1>www.baidu.com</html>中的地址
(1)
```py
import re
string = "<html><h1>www.baidu.com</html>"
regular_expression = re.compile('www\..+\.com')    #www.任意字符.com
print(regular_expression.search(string).group(0))
```
(2) 这种方式也可以进行匹配，不同的地方是正则表达式更精确
```py
import re
string = "<html><h1>www.baidu.com</html>"
print(re.search('(www\..+\.com)(www\..+\.html)',string).groups())
```




### 81 a="张明98分"，用re.sub，将98替换为100
```py
import re
a = "张明98分"
print(re.sub('98','100',a))
```





### 82正则表达式匹配中(.*)和(.*?)匹配区别？
加？会将贪婪模式改成懒惰模式,如果没有括号的话，则表示匹配0个或1个问号前面的表达式，非贪婪模式








### 83写一段匹配邮箱的正则表达式
(1)
```py
import re
mail_string = '5dasdfAA5@soho.net'
print(re.search('[0-9a-zA-Z_]*@.+\.(com|cn|net)$',mail_string).group())
```
(2)
```py
import re
mail_string = '5dasdfAA5@soho.net,123456@126.com'
print(re.findall('[0-9a-zA-Z_]+@[0-9a-zA-Z_]+\.(?:com|cn|net)',mail_string))
```








## 其他内容


### 84解释一下python中pass语句的作用？
Python pass 是空语句，是为了保持程序结构的完整性。
pass 不做任何事情，一般用做占位语句




### 85简述你对 input()函数的理解
```py
result = input('put in something please:')
print(result)
print(type(result))
```
input()函数接收一个标准的输入的数据，返回string类型




### 86 python中的is和==


Python中对象包含的三个基本要素，分别是：id(身份标识)、type(数据类型)和value(值)。
is和==都是对对象进行比较判断作用的，但对对象比较判断的内容并不相同。
下面来看看具体区别在哪。
==是python标准操作符中的比较操作符，用来比较判断两个对象的value(值)是否相等
```py
>>> a = 'cheesezh'
>>> b = 'cheesezh'
>>> a == b
True
```
is也被叫做同一性运算符，这个运算符比较判断的是对象间的唯一身份标识，也就是id是否相同
```py
>>> x = y = [4,5,6]
>>> z = [4,5,6]
>>> x == y
True
>>> x == z
True
>>> x is y
True
>>> x is z
False
>>>
>>> print id(x)
>>> print id(y)
>>> print id(z)
```


### 87 Python 中的作用域

python中的作用域遵循LEGB原则：
| charactor | name      | chinese            |
| --------- | --------- | ------------------ |
| L         | Local     | 局部作用域         |
| E         | Enclosing | 闭包函数外的函数中 |
| G         | Global    | 全局作用域         |
| B         | Built-in  | 内建作用域         |


python按照LEGB原则搜索变量，即优先级L>E>G>B 例如：


```py
print(type(list))        #list为   builtins
list = 1
print(list)
a = 3                #globals
def func1( ):
     a = 3            #enclosing
     def func2( ):
         a = 4        #locals
     return func2
```










### 88 三元运算写法和应用场景？


1. y = 99 if x > 3 else 999
2. result = {True:1, False:2}[a>b]
3. result = ('FalseValue','TrueValue')[a>b]

只要符合条件符合要求都可以应用吧，问的什么破问题






### 89 了解 enumerate 么？
enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中
例：
普通的for循环
```py
>>>i = 0 
>>> seq = ['one', 'two', 'three'] 
>>> for element in seq: 
... print i, seq[i] 
... i +=1 
... 
0 one 
1 two 
2 three
```
使用enumerate的for循环
```py
>>>seq = ['one', 'two', 'three'] 
>>> for i, element in enumerate(seq): 
... print i, element 
... 
0 one 
1 two 
2 three
```


### 90 列举 5 个 Python 中的标准模块


time，sys，os，datetime，random, shutil, re




### 91 如何在函数中设置一个全局变量


global a




### 92 pathlib 的用法举例


引用网址：
https://www.jianshu.com/p/a820038e65c3
```py
from pathlib import Path
p = Path(r'd:\test\tt.txt.bk')
p.name                          # 获取文件名
p.stem                          # 获取文件名除后缀的部分
p.suffix                        # 文件后缀
p.suffixs                       # 文件的后缀们...
# ['.txt', '.bk']
p.parent                        # 相当于dirnanme
# WindowsPath('d:/test')
p.parents                       # 返回一个iterable, 包含所有父目录
# <WindowsPath.parents>
for i in p.parents:
    print(i)
# d:\test
# d:\
a.parts                         # 将路径通过分隔符分割成一个元祖
# ('d:\\', 'test', 'tt.txt.bk')
```
遍历文件夹
```py
p = Path(r'd:\test')
p = Path(p, 'tt.txt')           # 字符串拼接
p.exists()                      # 判断文件是否存在
p.is_file()                     # 判断是否是文件
p.is_dir()                      # 判断是否是目录
```
创建文件夹
```py
p = Path(r'd:\test\tt\dd')
p.mkdir(exist_ok=True)          # 创建文件目录(前提是tt目录存在, 否则会报错)
# 一般我会使用下面这种创建方法
p.mkdir((exist_ok=True, parents=True) # 递归创建文件目录
```
文件信息
```py
p = Path(r'd:\test\tt.txt')
p.stat()                        # 获取详细信息
p.stat().st_size                # 文件大小
p.stat().st_ctime               # 创建时间
p.stat().st_mtime               # 修改时间
```


### 93 Python 中的异常处理，写一个简单的应用场景


异常处理语句try except finally
```py
def div(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Error: b should not be 0 !!")
    else:
        print('Run into else only when everything goes well')
    finally:
        print('Always run into finally block.')
```
try与except只有是分支选项只有一个可以执行，没有发生异常时else语句会执行，finally总是被执行




### 94 Python 中递归的最大次数，那如何突破呢？
```py
import sys
sys.setrecursionlimit(1500) # set the maximum depth as 1500
def recursion(n): 
    if(n <= 0): 
        return 
    print (n) 
    recursion(n - 1) 
if __name__ == "__main__":
    recursion(1469)
```
默认递归次数是1000，实际运行递归不报错大概是970左右，第二行是修改最大递归次数方法set recursion limit




### 95 什么是面向对象的 mro


mro, method resolution order 方法解析顺序
https://blog.csdn.net/wangjianno2/article/details/56672442  
or
https://blog.csdn.net/weixin_42104289/article/details/88528301




### 96 isinstance 作用以及应用场景？


用来判断一个量是否是相应的类型
print(isinstance(a,int)) #判断a是否为int类型




### 97 什么是断言？应用场景？


assert断言语句用来声明某个条件是真的，
其作用是测试一个条件是否成立，如果不成立则抛出异常
例1：
```py
assert (v1 > v2),'{0} is not bigger than {1}'.format(v1,v2)
```
如果`v1<v2`,则抛出的异常是：
```py
AssertionError: 1 is not bigger than 2
```
断言跟异常的区别：
断言是用来检查非法情况而不是错误情况的，用来帮开发者快速定位问题的位置。
异常处理用于对程序发生异常情况的处理，增强程序的健壮性和容错性




### 98 lambda 表达式格式以及应用场景？


例1：
```py
f = lambda x: x/2
```
f(6)的结果是3
例2：
```py
fs = [(lambda x,i=i:i/x) for i in range(10)]
```
如果上面的式子不写i=i，而是直接写i，此处的i是首先选用全局变量的，所以如果恰好有全局变量i，就会得出其他结果，要注意；
fs[6](2)的结果是3，[ ]内是i的值，（）内是x的值，这里需要说明一下，fs的type是list但是这里的list是用表达式表示的，所以有些不同，
```py
fs[2]
Out[105]: <function __main__.<listcomp>.<lambda>>
a = fs[2]
print(a(1))
2.0
```
如果是fs[:](3)或者fs(3)或者fs[11]都会报错，这是lambda与for迭代结合后的一些特性




### 99 新式类和旧式类的区别


* 新式类都从object继承，经典类不需要。
* 新式类的MRO(method resolution order 基类搜索顺序)算法采用C3算法广度优先搜索，而旧式类的MRO算法是采用深度优先搜索
* 新式类相同父类只执行一次构造函数，经典类重复执行多次。




### 100 dir()是干什么用的？


获得模块的属性列表




### 101 一个包里有三个模块，demo1.py, demo2.py, demo3.py，但使用 from  tools import *导入模块时，如何保证只有 demo1、demo3 被导入了。


增加__init__.py文件，并在文件中增加：__all__ = ['mod1','mod3']




### 102 列举 5 个 Python 中的异常类型以及其含义

| name              | explaination                                                                               |
| ----------------- | ------------------------------------------------------------------------------------------ |
| AttributeError    | 试图访问一个对象没有的树形，比如foo.x，但是foo没有属性x                                    |
| IOError           | 输入/输出异常；基本上是无法打开文件                                                        |
| ImportError       | 无法引入模块或包；基本上是路径问题或名称错误                                               |
| IndentationError  | 语法错误（的子类） ；代码没有正确对齐                                                      |
| IndexError        | 下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]                                  |
| KeyError          | 试图访问字典里不存在的键                                                                   |
| KeyboardInterrupt | Ctrl+C被按下                                                                               |
| NameError         | 使用一个还未被赋予对象的变量                                                               |
| SyntaxError       | Python代码非法，代码不能编译(个人认为这是语法错误，写错了）                                |
| TypeError         | 传入对象类型与要求的不符合                                                                 |
| UnboundLocalError | 试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，导致你以为正在访问它 |
| ValueError        | 传入一个调用者不期望的值，即使值的类型是正确的                                             |




### 103 copy 和 deepcopy 的区别是什么？


拷贝之前再说下 b =a，这种情况两者的id是一个
[[], []] 列表的嵌套, [{}, {}] 字典的嵌套，可变类型嵌套了可变类型, 
* 浅拷贝只拷贝最外层,会生成新的对象, 内层是引用, 
* 深拷贝外层和内层都会进行拷贝,都是全新的对象, 都有独立的存储空间
```py
In [22]: a = [11, 22]
In [23]: b = [33, 44] 
In [24]: c = [a, b]
In [25]: d = copy.copy(c)
In [26]: e = copy.deepcopy(c)


In [27]: id(c)
Out[27]: 2644923219336
In [28]: id(d)
Out[28]: 2644923160392
In [29]: id(e)
Out[29]: 2644923143624
In [30]: id(a)
Out[30]: 2644913732296
In [32]: id(d[0])
Out[32]: 2644913732296
In [33]: id(e[0])
Out[33]: 2644923077512
```


### 104 代码中经常遇到的*args, **kwargs 含义及用法。


https://blog.csdn.net/lcxxcl_1234/article/details/80726668
*args和**kwargs主要用于函数定义。可以将不定数量的参数传递给某个函数
*args是用来发送一个非键值对的可变数量的参数列表给一个函数


`**kwargs`允许你将不定长度的键值对作为参数传递给一个函数。如果你想要在一个函数里处理带名字的参数，你应该使用`**kwargs`


其实关键是*与**，而args与kwargs换成其他也可以，只不过是一种常见的写法




### 105 Python 中会有函数或成员变量包含单下划线前缀和结尾，和双下划线前缀结尾，区别是什么？


* _xxx
单下划线开头的变量，表明这是一个`受保护（protected）的变量`，原则上不允许直接访问
但是外部类还是可以访问到这个变量。


* __xxx
双下划线开头的，表示的是`私有类型（private）的变量`，只能允许这个类本身进行访问，甚至它的子类也不可以，用于命名一个类属性（类变量），调用时名字会被改变
可以通过dir（sd）查看变量，通过python的私有变量碾压特性，sd.__name变成了sd._Student__name。Python把以两个或以上下划线字符开头且没有以两个或以上下划线结尾的变量当作私有变量。私有变量会在代码生成之前被转换为长格式（变为公有）。转换机制是这样的：在变量前端插入类名，再在前端加入一个下划线字符。这就是所谓的私有变量碾压（Private name mangling）


* __xxx__
以双下划线开头，并且以双下划线结尾的，是`内置变量`，内置变量是可以直接访问的，如__init__,__import__或是__file__。所以，不要自己定义这类变量。
添加个进阶的链接：
https://www.cnblogs.com/hester/articles/4936603.html




### 106 w、a+、wb 文件写入模式的区别


* w：只写模式，文件不存在则新建文件，文件指针在文件开头，会清空原来的文件内容
* a+：读写模式，文件不存在新建文件，文件指针位于文件结尾，不会清空原来文件内容，可在任意位置读取，但只能在文件末尾写入
* wb：与w的区别是，wb打开的是二进制模式，w打开的是文本模式，所有带'b'的都是二进制模式打开




### 107 举例 sort 和 sorted 的区别


使用sort()方法对list排序会修改list本身,不会返回新list，sort()不能对dict字典进行排序；
sorted方法对可迭代的序列排序生成新的序列，对dict排序默认会按照dict的key值进行排序，最后返回的结果是一个对key值排序好的list；
python2.4开始，list.sort()与sorted()增加了key参数，具体用法请自查




### 108 什么是负索引？


负索引就是像a[-1]，表示从末尾向前数的第一个




### 109 pprint 模块是干什么的？


pprint是打印模块，与print的区别是pprint打印出来的数据结构更加完整；
所谓的完整一般就是分行打印，每行一个数据结构，方便阅读；




### 110 解释一下 Python 中的赋值运算符






### 111 解释一下 Python 中的逻辑运算符




### 112    讲讲 Python 中的位运算符




### 113  在 Python 中如何使用多进制数字？


* 二进制：0bxxxx，
  * 转为二进制：bin(xxx)
* 八进制：0oxxxx，
  * 转为八进制：oct(xxx)
* 十进制：xxxx，
  * 转为十进制：dec(xxx)
* 十六进制：0x****
  * 转为十六进制：hex(xxx)




### 114 怎样声明多个变量并赋值？


多个变量赋值：
```py
a,b = 1,2
```
多个变量声明并赋值：
```py
for i in range(10):
    cmd = "var_%s = i" % i
    exec (cmd)
    #eval("var_%s" % i)
print (var_5)
```
结果：5


---------------------------------------------------------------------------------------------
## 算法和数据结构




### 115  已知：


AList = [1,2,3]
BSet = {1,2,3}
(1)    从 AList和BSet中查找4，最坏时间复杂度那个大？
(2)    从 AList和BSet中插入4，最坏时间复杂度那个大？
需要弄清楚列表与哈希表的区别：
对于查找，列表的时间复杂度是O(n), set是O(1)
对于插入，两个都是O(1)
可以关注下链接，讲的python数据结构与算法，很不错
https://www.cnblogs.com/pengsixiong/p/5304065.html




### 116 用 Python 实现一个二分查找的函数
```py
def dichotomy_search(list_f,target_d):
    start = 0
    end = len(list_f)-1
    find_state = False
    while start <= end and not find_state:
        midpoint = (start+end)//2
        #print(midpoint)
        if list_f[midpoint] < target_d:
            start = midpoint + 1
        elif list_f[midpoint] > target_d:
            end = midpoint - 1
        else:
            find_state = True
    return (find_state,midpoint)
list_f = [1,2,3,4,5,6,7,8,9,11,23,45]
#target_d = 8
result = dichotomy_search(list_f,3)
print(result)
```


### 117 python 单例模式的实现方法


单例模式就是一个类只能创建一个实例化，创建的所有实例化的id都是相同的
单例模式实现有两种方式，


1.    使用__metaclass__元类来实现
```py
class Singleton(type):    
    def __init__(cls, name, bases, dict):    
        super(Singleton, cls).__init__(name, bases, dict)    
        cls._instance = None    
    def __call__(cls, *args, **kw):    
        if cls._instance is None:    
            cls._instance = super(Singleton, cls).__call__(*args, **kw)    
        return cls._instance

class MyClass(metaclass=Singleton):  
    def __init__(self,name):
        self.name = name

a = MyClass('')
print(a)
b = MyClass('')
print(b)
```


2. 使用装饰器（decorator）
```py
def singleton(cls, *args, **kw):    
    instances = {}    
    def _singleton():    
        if cls not in instances:    
            instances[cls] = cls(*args, **kw)    
        return instances[cls]    
    return _singleton    
@singleton    
class MyClass(object):    
    a = 1    
    def __init__(self, x=0):    
        self.x = x     
```


3. 使用模块
Python 的模块就是天然的单例模式，因为模块在第一次导入时，会生成 .pyc 文件，当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码。
因此，我们只需把相关的函数和数据定义在一个模块中，就可以获得一个单例对象了
```py
class Singleton(object):
    def foo(self):
        pass
singleton = Singleton()
```
保存为mysingleton.py文件
form * import singleton 这样就ok了


4. 重写__new__方法
* 重写__new__方法一定要`return super().__new__(cls)`
* 否则，Python据诶时期得不到分配了空间的对象引用，就不会调用对象的初始化方法
* 注意：__new__是一个静态方法，在调用时需要主动传递cls参数

```py
class MusicPlayer(object):
    instance = None
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

o1 = MusicPlayer()
print(o1)
o2 = MusicPlayer()
print(o2)
```

```py
# 运行结果
PS E:\OneDrive\Doc\MD.Lang\Python> & C:/Python37/python.exe e:/设计模式/单例模式/codes/new实现.1.py
Init MusicPlayer..
<__main__.MusicPlayer object at 0x0000012614CCC748>
Init MusicPlayer..
<__main__.MusicPlayer object at 0x0000012614CCC748>
PS E:\OneDrive\Doc\MD.Lang\Python>
```


这是比较简单易实现的方法还有其他比如类方法等等




### 1   使用 Python 实现一个斐波那契数列


1. 用递归方式打印第n项
```py
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return(1)
    elif n == 2:
        return(1)
    else:
        return(fibonacci(n-1)+fibonacci(n-2))
print(fibonacci(10))
```


2. 常规方法打印前n项数列
```py
def fibonacci(n):
    list_f = [0,1]
    if n > 1:
        for i in range(n-1):
            list_f.append(list_f[i]+list_f[i+1])   
    return(list_f[:n])        
print(fibonacci(10))
```


### 1   找出列表中的重复数字


1. 用count计数

```py
mylist = [1,2,2,2,2,3,3,3,4,4,4,4]
myset = set(mylist)
for item in myset:
    print("the %d has found %d" %(item, mylist.count(item)))
```

2. 用 collections counter
```py
from collections import Counter
    result = Counter([1,2,2,2,2,3,3,3,4,4,4,4])
    print(result)
```

需要说明，结果是dict，输出的结果是Counter({2: 4, 4: 4, 3: 3, 1: 1})




### 1   找出列表中的单个数字


在119的1基础上稍微修改就可以




### 1   写一个冒泡排序
```py
list_f = [12,32,31,52,17,6,19,10]
def bubble_sort(list_f):
    length_list = len(list_f)
    while(length_list>1):
        for i in range(length_list-1):
            if list_f[i] > list_f[i+1]:
                inmed_var = list_f[i]
                list_f[i] = list_f[i+1]
                list_f[i+1] = inmed_var
        length_list = length_list-1
        print(length_list)
    return list_f
print(bubble_sort(list_f))
```


### 1   写一个快速排序


快速排序常用且重要，这里总结出3种排序方式：


1. 表达式方式
```py
array = [2,5,6,1,2,89,34,21,3]
quick_sort = (
            lambda array: array if len(array) <= 1 else
            quick_sort([item for item in array[1:] if item <= array[0]]) 
            + [array[0]] 
            + quick_sort([item for item in array[1:] if item > array[0]])
            )
print(quick_sort(array))
```
通过一个表达式完成，有两点说明:
长表达式换行有两种方式一个是( ) or [ ] or { }，另一种就是在想要换行的位置加'\'
另一个是，用lambda实现递归时，公式中的递归quick_sort( )括号内的内容是在当前执行出结果然后将list给递归函数，换句话说就是quick_sort([item for item in array[1:] if item <= array[0]])这个公式，递归时quick_sort(list)，是这种模式，然后list是[item for item in array[1:] if item <= array[0]]的运行后的结果。

2. 一般思路的块排
```py
array = [2,5,6,1,2,89,34,21,3]
def quick_sort(array, left, right):
    if left >= right:
        return
    low = left
    high = right
    key = array[low]
    while left < right:
        while left < right and array[right] > key:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= key:
            left += 1
        array[right] = array[left]
    array[right] = key
    quick_sort(array, low, left - 1)
    quick_sort(array, left + 1, high)
quick_sort(array,0,8)
print(array)
```
感觉还是比较绕的，多在纸上写一下推到一下可能会更容易理解；

3. 这种方法相对简洁一些
```py
array = [2,5,6,1,12,89,34,21,3]
def quick_sort(array, l, r):
    if l < r:
        q = partition(array, l, r)
        quick_sort(array, l, q - 1)
        quick_sort(array, q + 1, r)
def partition(array, l, r):
    x = array[r]
    i = l - 1
    for j in range(l, r):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i+1]
    return i + 1
quick_sort(array,0,len(array)-1)
print(array)
```

4. 用栈的方式实现非递归的快排程序
```py
array = [2,5,6,1,12,89,34,21,3]
def quick_sort(array, l, r):
    if l >= r:
        return
    stack = [ ]
    stack.append(l)
    stack.append(r)
    print(stack)
    while stack:
        low = stack.pop(0)
        high = stack.pop(0)
        if high - low <= 0:
            continue
        x = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= x:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        stack.extend([low, i, i + 2, high])
        print(stack)
quick_sort(array,0,len(array)-1)
print(array)
```
快排的几种实现方式都不是很好理解




### 1   写一个拓扑排序
```py
def toposort(graph):
    in_degrees = dict((u,0) for u in graph)   #初始化所有顶点入度为0
    vertex_num = len(in_degrees)
    for u in graph:
        for v in graph[u]:
            in_degrees[v] += 1       #计算每个顶点的入度
    Q = [u for u in in_degrees if in_degrees[u] == 0]   # 筛选入度为0的顶点
    Seq = []
    while Q:
        u = Q.pop()       #默认从最后一个删除
        Seq.append(u)
        for v in graph[u]:
            in_degrees[v] -= 1       #移除其所有指向
            if in_degrees[v] == 0:
                Q.append(v)          #再次筛选入度为0的顶点
    if len(Seq) == vertex_num:       #如果循环结束后存在非0入度的顶点说明图中有环，不存在拓扑排序
        return Seq
    else:
        print("there's a circle.")
G = {'a':'bce','b':'d','c':'bd','d':'','e':'cd'}
print(toposort(G))
```


### 1   python 实现一个二进制计算


这个题目的真正目的我没有太理解，
如果理解成二进制的转化，bin( )也可以直接完成，不过这里需要注意的是，type(bin())是str，如果str进行加法，是将两个字符串拼接，并不是我们想要的计算
如果c = 0b11011，type(c)是intpython是没有二进制这个数据格式的，如果要实现只能转化成int计算后转回二进制形式
如果非要代码的形式实现二进制的+-*/，可能会繁琐一点，这里略




### 1   有一组"+"和"-"符号，要求将"+"排到左边，"-"排到右边，写出具体的实现方法。
```py
target = '+--++++--'
result1 = []
result2 = []
for i in target:
    if i == '+':
        result1.append(i)
    else:
        result2.append(i)
result1.extend(result2)
print(result1)
print(('').join(result1))
```


### 1   单链表反转
```py
class Node(object):
    def __init__(self, data, next=None):
        self.val = data
        self.next = next

def fun4(head):
    if head == None:
        return None
    L,M,R = None,None,head
    while R.next != None:
        L = M
        M = R
        R = R.next
        M.next = L
    R.next = M
    return R
#测试用例
if __name__ == '__main__':
    l1 = Node(3)
    l1.next = Node(2)
    l1.next.next = Node(1)
    l1.next.next.next = Node(9)
    l = fun4(l1)
    print (l.val, l.next.val, l.next.next.val, l.next.next.next.val)
```


### 1   交叉链表求交点
```py
class ListNode:
    def init(self, x):
        self.val = x
        self.next = None
    def node(l1, l2):
        length1, length2 = 0, 0
        # 求两个链表长度
        while l1.next:
            l1 = l1.next
            length1 += 1
        while l2.next:
            l2 = l2.next
            length2 += 1
        # 长的链表先走
        if length1 > length2:
            for _ in range(length1 - length2):
                l1 = l1.next
        else:
            for _ in range(length2 - length1):
                l2 = l2.next
        while l1 and l2:
            if l1.next == l2.next:
                return l1.next
            else:
                l1 = l1.next
                l2 = l2.next
```


### 1   用队列实现栈


队列是先进先出，栈是先进后出，如果非要把队列当栈来实现的话，如下：
```py
from collections import deque
queue = deque(["a"])
queue.append("b")
queue.append("c")
for _ in range(3):                                
print(queue.pop())
```
如果是queue.popleft( )的话，就符合先进先出的特性了；这个功能的实现其实是导入了tensorflow的包，算是钻了个空子吧。




### 1   找出数据流的中位数
```py
import heapq
class BigHeap():
    def __init__(self):
        self.arr = list()
    def heap_insert(self, val):
        heapq.heappush(self.arr, -val)
    def heapify(self):
        heapq.heapify(self.arr)
    def heap_pop(self):
        return -heapq.heappop(self.arr)
    def get_top(self):
        if not self.arr:
            return
        return -self.arr[0]
class SmallHeap():
    def __init__(self):
        self.arr = list()
    def heap_insert(self, val):
        heapq.heappush(self.arr, val)
    def heapify(self):
        heapq.heapify(self.arr)
    def heap_pop(self):
        return heapq.heappop(self.arr)
    def get_top(self):
        if not self.arr:
            return
        return self.arr[0]
class MedianHolder():
    def __init__(self):
        self.bigHeap = BigHeap()
        self.smallHeap = SmallHeap()
    def addNum(self, num):
        if len(self.bigHeap.arr) == 0:
            self.bigHeap.heap_insert(num)
            return
        if self.bigHeap.get_top() >= num:
            self.bigHeap.heap_insert(num)
        else:
            if len(self.smallHeap.arr) == 0:
                self.smallHeap.heap_insert(num)
                return
            if self.smallHeap.get_top() > num:
                self.bigHeap.heap_insert(num)
            else:
                self.smallHeap.heap_insert(num)
        self.modifyTwoHeapSize()
    def getMedian(self):
        smallHeapSize = len(self.smallHeap.arr)
        bigHeapSize = len(self.bigHeap.arr)
        if smallHeapSize + bigHeapSize == 0:
            return None
        smallHeapHead = self.smallHeap.get_top()
        bigHeapHead = self.bigHeap.get_top()
        if (smallHeapSize + bigHeapSize) %2 == 0:
            return (smallHeapHead+bigHeapHead)/2
        else:
            return smallHeapHead if smallHeapSize > bigHeapSize else bigHeapHead
    def modifyTwoHeapSize(self):
        smallHeapSize = len(self.smallHeap.arr)
        bigHeapSize = len(self.bigHeap.arr)
        if smallHeapSize == bigHeapSize + 2:
            self.bigHeap.heap_insert(self.smallHeap.heap_pop())
        if bigHeapSize == smallHeapSize + 2:
            self.smallHeap.heap_insert(self.bigHeap.heap_pop())
if __name__ == '__main__':
    arr = [68,51,42,92,13,46,24,58,62,72,32]
    medianHold = MedianHolder()
    for i in range(len(arr)):
        medianHold.addNum(arr[i])
        print(medianHold.getMedian())
```


关于heapq的说明见以下链接：
https://rookiefly.cn/detail/225




### 1   二叉搜索树中第 K 小的元素


1.递归
```py
class Solution(object):
    def kthSmallest(self, root, k):
        self.count=k
        self.res=0
        def core(root):
            if  root :
                core(root.left)
                self.count=self.count-1
                if self.count==0:
                    self.res=root.val 
                core(root.right)
        core(root)
        return self.res
```
2.循环
```py
class Solution(object):
    def kthSmallest(self, root, k):
        stack=[]
        while True:
            if root:
                stack.append(root)
                root=root.left
            else:
                root=stack.pop()
                k=k-1
                if k==0:
                    return root.val
                else:
                    root=root.right
```




## 爬虫问题




### 1   在 requests 模块中，requests.content 和 requests.text 什么区别


可以参考这个链接：
https://blog.csdn.net/xie_0723/article/details/51361006
内容概括如下
区别总结就是：
requests.text返回的是Unicode型的数据。
requests.content返回的是bytes型也就是二进制的数据
操作方式就是，如果想取得文本就用.text，如果想获取图片，就用.content
给个例子：
```py
import requests
jpg_url = 'http://img2.niutuku.com/1312/0804/0804-niutuku.com-27840.jpg'
content = requests.get(jpg_url).content
with open('demo.jpg', 'wb') as fp:
    fp.write(content)
```


### 1   简要写一下 lxml 模块的使用方法框架


lxml是处理网页数据的第三方库，用Cython实现。
细节参考链接：
https://www.cnblogs.com/ospider/p/5911339.html




### 133说一说 scrapy 的工作流程


1. 首先Spiders（爬虫）将需要发送请求的url(requests)经ScrapyEngine（引擎）交给Scheduler（调度器）。
2. Scheduler（排序，入队）处理后，经ScrapyEngine，DownloaderMiddlewares(可选，主要有User_Agent, Proxy代理)交给Downloader。
3. Downloader向互联网发送请求，并接收下载响应（response）。将响应（response）经ScrapyEngine，SpiderMiddlewares(可选)交给Spiders。　　　　　
4. Spiders处理response，提取数据并将数据经ScrapyEngine交给ItemPipeline保存（可以是本地，可以是数据库）。
5. 提取url重新经ScrapyEngine交给Scheduler进行下一个循环。直到无Url请求程序停止结束

https://blog.csdn.net/miner_zhu/article/details/81094077
