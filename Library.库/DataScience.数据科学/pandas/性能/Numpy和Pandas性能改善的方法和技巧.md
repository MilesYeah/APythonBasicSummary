
# [ Numpy和Pandas性能改善的方法和技巧 ](https://mp.weixin.qq.com/s/9LCK7htiXCwSNdvh6BSKDg)


Numpy和Pandas性能改善的方法和技巧
原创 大邓 大邓和他的Python 4月26日
问题

    设计的代码能hold住小规模数据
    你准备将该代码用来处理真实场景的数据
    但惊喜的是你的代码崩溃了
    问题: 你的电脑只有16G内存，但现在却要应付50G大小的数据。




硬件解决办法

    换装备，比如64G内存的电脑
    租用云服务器，64核432G内存，每小时几十元

软件解决办法

    压缩你的数据
    分块读取，一次只读一块。
    对数据进行索引标注，只在需要的时候导入内存

本教程涉及

numpy和pandas的三种思维来处理内存占用和性能问题

    压缩
    分块
    索引

一、 压缩

    指的是同样的信息量数据，使用更少的内存。
    在内存上压缩，而非在硬盘里压缩

1.1 压缩：Numpy dtype

ss
numpy类型	介绍	数值范围
np.int8	字节	（-128 to 127）
np.int16	整数	（-32768 to 32767）
np.int32	整数	（-2147483648 to 2147483647）
np.int64	整数	（-9223372036854775808 to 9223372036854775807）
np.uint8	无符号整数	（0 to 255）
np.uint16	无符号整数	（0 to 65535）
np.uint32	无符号整数	（0 to 4294967295）
np.uint64	无符号整数	（0 to 18446744073709551615）
np.float16	半精度浮点数，包括：1 个符号位，5 个指数位，10 个尾数位	
np.float32	单精度浮点数，包括：1 个符号位，8 个指数位，23 个尾数位	
np.float64	双精度浮点数，包括：1 个符号位，11 个指数位，52 个尾数位	


同样的整数，用np.int64占用的内存是np.int16的4倍

import numpy as np

int64arr = np.ones((1024, 1024), dtype=np.int64)
int16arr = np.ones((1024, 1024), dtype=np.int16)

#占用（内存）的字节数
print(int64arr.nbytes)
print(int16arr.nbytes)

8388608
2097152

1.2 压缩: 稀疏的数组

https://sparse.pydata.org/

    数组中有大量的0
    内存浪费在很多0身上
    稀疏数据只存储非0数据
    用numpy数组对数据进行插值
    不同的表达数据的方式

sparse可以压缩数据内存占用量，看一个例子

import numpy as np

arr = np.random.random((1024, 1024))
arr[arr < 0.9] = 0

print(arr)

[[0.         0.         0.         ... 0.         0.94559922 0.        ]
 [0.         0.         0.         ... 0.         0.         0.        ]
 [0.         0.         0.         ... 0.         0.         0.        ]
 ...
 [0.94589484 0.         0.         ... 0.96746948 0.         0.        ]
 [0.         0.         0.         ... 0.96236294 0.         0.        ]
 [0.         0.         0.         ... 0.         0.         0.        ]]

import sparse #需要安装sparse
sparse_arr = sparse.COO(arr)
print(sparse_arr)

<COO: shape=(1024, 1024), dtype=float64, nnz=104998, fill_value=0.0>

print(arr.nbytes)
print(sparse_arr.nbytes)

8388608
2519952

1.3 压缩: Pandas dtype

如果知道数据的字段，可以在pandas导入数据时就设定字段的dtype参数，减少不必要的内存开支。例如

import pandas as pd
import numpy as np

#不设定dtype
df1 = pd.read_csv('data.csv')
df1

trip_id是整数，默认pandas用的是np.int64, 我们可以将其设定为np.int32

#设定dtype参数
df2 = pd.read_csv('data.csv', dtype={"trip_id": np.int32})
df2

print(df1['trip_id'].nbytes)
print(df2['trip_id'].nbytes)

40
20

我们可以看到通过指定dtype，trip_id字段占用的内存少了一半。
二、 分块
2.1 分块处理全部的数据

也可以分块处理全部的数据，最后将结果再汇总，减少电脑的内存压力。比如我们想求长度为1024的数组arr中的最大值

import numpy as np

#长度1024的数组arr
arr = np.random.random(1024)

arr

array([0.37143228, 0.14093017, 0.67051473, ..., 0.42278493, 0.38588344,
       0.11637298])

#一次性求最大
max(arr)

0.9994997367530419

#分块，汇总求最大
max(max(arr[:500]), max(arr[500:]))

0.9994997367530419

2.2 分块：Pandas也能分块

分块依次读取，这样可以对比电脑内存还大的数据进行运算操作。

import pandas as pd

max_record = 0

#分块依次读取，专业
for chunk in pd.read_csv('my.csv',
                         chunksize=100):#块的记录数为100条
    max_record = max(
        max_record,
        max(chunk['某个需要求最大值的字段名'])
    )
    
print(max_record)

598000
2.3 并行: 对很多块并行处理

    如果数据块之间彼此独立
    且对数据块的计算也是独立的
    我们可以利用电脑多核进行并行运算
    并不会降低内存占用，但是会提高运行速度

块的大小，需要满足

    64G内存， 并行数为1时，处理的块数据大小不超过60G
    64G内存， 并行数为4时，处理的块数据大小不超过15G

三、索引
3.1 索引：需要的时候再调用

    索引是对数据的准确描述
    索引对应的数据一定比内存小很多
    索引能告诉程序数据的子集在哪里

3.2 索引 vs 分块

    分块需要导入所有的数据， "What is the longest word in this book?"需要研究这本书的每一页。

    索引只导入数据的子集, "How much money did we spend in July?"，只需要在意July，其他月份不用考虑。

    两者经常搭配使用

3.3 索引：Pandas不支持索引

所以需要自定义,实现索引功能

def get_subset(csvf, field, conditon):
    """
    从csv数据中抽取出field值为condition的所有数据。
    csvf: csv文件的路径
    field: 需要的字段
    conditon: 字段field需要满足的条件
    """
    return pd.concat(
        df[df.field==conditon] 
        for df in pd.read_csv(csvf, chunksize=1000)
    )

3.4 索引: SQLite&pandas

如何让sqlite数据库也能分块

import sqlite

def create_index(csvf, dbname, field):
    """
    将csv中的数据转移至sqlite数据库，并给field创建索引
    dbname: sqlite数据库库名
    field: 需要创建索引的字段名
    """
    db=sqlite.connect("{}.sqlite".format(dbname))

    for chunk in pd.read_csv(csvf, chunksize=1000):
        chunk.to_sql(dbname, db, if_exists='append')

    db.execute("CRESTE INDEX {field} ON {dbname}({field})".format(field=field, dbname=dbname, field=field))
    db.close()

def get_subset(dbname, field, conditon):
    """
    从dbname中抽取出field值为condition的所有数据。
    dbname: sqlite数据库库名
    field: 需要的字段
    condition: 字段field需要满足的条件
    """
    conn = sqlite3.connect("{}.sqlite".format(dbname))
    q = ("SELECT * FROM {db} WHERE {field} = {condtion}".format(db=dbname, field=field, condition=conditon))
    return pd.read_sql_query(q, conn)

3.5 索引：SQLite vs csv

使用70k voters数据对比

    Cambridge,MA : 70k voters

类型	操作	内存占用情况
CSV	分块依次读取10000行 + 按条件找出需要的数据	574ms
SQLite	索引找出需要的数据	10ms
总结

    同样的问题

    内存快但贵
    硬盘便宜但慢

    解决办法：压缩、分块（有条件的并行）、索引
    对了，如果不差钱，事情会好办不少。。。

公众号后台回复关键词 pandas_numpy, 可获得该数据集
往期文章

中文文本分析相关资源汇总

cnsenti中文情绪情感分析库

70G上市公司定期报告数据集

如何计算出文本数据的相似矩阵？

两行代码读取pdf、docx文件

三行代码计算文本相似性

5个小问题带你理解列表推导式

文本数据清洗之正则表达式

Python网络爬虫与文本数据分析

综述:文本分析在市场营销研究中的应用

LabelStudio多媒体数据标注工具[5星推荐]

如何批量下载上海证券交易所上市公司年报

Loughran&McDonald金融文本情感分析库

如何使用Python快速构建领域内情感词典

Python数据分析相关学习资源汇总帖

漂亮~pandas可以无缝衔接Bokeh

YelpDaset: 酒店管理类数据集10+G


看在这么多数据面子上，给我点好看可好❤


微信扫一扫
关注该公众号
