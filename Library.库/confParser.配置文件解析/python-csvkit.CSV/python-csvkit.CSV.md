如果你在学Python数据处理，一定对CSV文件不陌生。日常本地数据存储中，除了Excel文件外，大部分数据都是以CSV文件格式保存的。

CSV（Comma-Separated Values）是一种文本文件，也叫作逗号分隔值文件格式。顾名思义，它就是用来保存纯文本，被分隔符分隔为多个字段。

CSV文件能够被Excel、notepad++、Java、Python等各种软件读取，非常方便。

因为它结构简单、易传输、易读取的特性，使其广受个人和商业领域欢迎。
图片

在Python中，可以使用read函数、pandas库、csv库等读写CSV文件，而且这些也是常用的方法。

这次给大家介绍一个非常强大的第三方库-csvkit，它是专门处理CSV文件的命令行工具，可以实现文件互转、数据处理、数据统计等，十分便捷。

因为csvkit是Python第三方库，我们直接使用pip来安装csvkit。
```py
pip install csvkit
```
csvkit是命令行工具，所以代码都在命令行执行，下面列举一些常见的使用场景。

我们先在本地保存一个Excel表（DoubanMovie），其内容是豆瓣电影数据。
图片

注意命令行地址要切换到该表所在位置。

比如我放在E:\csvkit_tutorial\里面，可以用下面命令来切换。
```
E：
cd csvkit_tutorial
```



## 1、Excel转CSV

csvkit支持将Excel等其他数据文件转化为CSV文件，使用in2csv命令实现。
```
in2csv DoubanMovie.xlsx > DoubanMovie.csv
```
除了Excel的xlsx和xls文件外，你还可以对下面多种数据格式进行CSV的转换

包括：dbf , fixed , geojson , json , ndjson





## 2、对SQL数据库进行读写和查询操作

从MySQL数据库中读取一张表存到本地CSV文件中，使用csvsql命令实现。
```
csvsql --db "mysql://user:pass@host/database?charset=utf8" --tables "test1" --insert test1.csv
```
直接对MySQL数据库进行数据查询，使用sql2csv命令实现
```
sql2csv --db "mysql://user:pass@host/database?charset=utf8" --query "select * from test2"
```
注意代码中--db参数后面需要输入数据库的信息，用于连接数据库。





## 3、将CSV文件转换为Json格式

除了将Json文件转化为CSV格式外，csvkit也支持将CSV文件转化为Json格式，使用csvjson命令实现。
```
csvjson test.csv
```
如果你是做地理空间分析，还可以将csv文件转化为GeoJson格式。






## 4、数据处理和分析

csvkit中还有用于数据处理分析的命令，如下：

* csvcut：对数据进行索引切片
* csvgrep：对数据进行过滤，可按照正则表达式规则
* csvjoin：对不同数据表按键进行连接
* csvsort：对数据进行排序
* csvstack：将多个数据表进行合并
* csvlook：以 Markdown 兼容的固定宽度格式将 CSV 呈现到命令行
* csvstat：对数据进行简单的统计分析





## 小结

csvkit适合那些经常处理CSV文件的小伙伴，可快速的进行转化、清晰、分析等任务。特别当你的文件较大，一般软件难以打开时，csvkit的速度绝对会让你惊艳到。







## ref
* [学习文档：](https://csvkit.readthedocs.io/en/latest/index.html)
* [ 强大的CSV文件命令行工具：python-csvkit ](https://mp.weixin.qq.com/s/EEHFMr_J6FExrDBjprISpA)
* []()
* []()
* []()
* []()
* []()

