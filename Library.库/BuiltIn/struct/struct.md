# [python之struct详解](https://blog.csdn.net/qq_30638831/article/details/80421019)

## 用处
* 按照指定格式将Python数据转换为字符串,该字符串为字节流,如网络传输时,不能传输int,此时先将int转化为字节流,然后再发送;
* 按照指定格式将字节流转换为Python指定的数据类型;
* 处理二进制数据,如果用struct来处理文件的话,需要用’wb’,’rb’以二进制(字节流)写,读的方式来处理文件;
* 处理c语言中的结构体;


## struct模块中的函数
| 函数                                | return      | explain                                                                                                                  |
| ----------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------ |
| pack(fmt,v1,v2…)                    | string      | 按照给定的格式(fmt),把数据转换成字符串(字节流),并将该字符串返回.                                                         |
| pack_into(fmt,buffer,offset,v1,v2…) | None        | 按照给定的格式(fmt),将数据转换成字符串(字节流),并将字节流写入以offset开始的buffer中.(buffer为可写的缓冲区,可用array模块) |
| unpack(fmt,v1,v2…..)                | tuple       | 按照给定的格式(fmt)解析字节流,并返回解析结果                                                                             |
| pack_from(fmt,buffer,offset)        | tuple       | 按照给定的格式(fmt)解析以offset开始的缓冲区,并返回解析结果                                                               |
| calcsize(fmt)                       | size of fmt | 计算给定的格式(fmt)占用多少字节的内存，注意对齐方式                                                                      |


## 格式化字符串
当打包或者解包的时,需要按照特定的方式来打包或者解包.该方式就是格式化字符串,它指定了数据类型,除此之外,还有用于控制字节顺序、大小和对齐方式的特殊字符.

## 对齐方式
为了同c中的结构体交换数据，还要考虑c或c++编译器使用了字节对齐，通常是以4个字节为单位的32位系统，故而struct根据本地机器字节顺序转换.可以用格式中的第一个字符来改变对齐方式.定义如下

| Character | Byte order    | Size | Alignment       |
| --------- | ------------- | ---- | --------------- |
| @(默认)   | 本机          | 本机 | 本机,凑够4字节  |
| =         | 本机          | 标准 | none,按原字节数 |
| <         | 小端          | 标准 | none,按原字节数 |
| >         | 大端          | 标准 | none,按原字节数 |
| !         | network(大端) | 标准 | none,按原字节数 |

如果不懂大小端,见大小端参考网址.


## 格式符
| 格式符     | C语言类型          | Python类型         | Standard size |
| ---------- | ------------------ | ------------------ | ------------- |
| x          | pad byte(填充字节) | no value           |
| c          | char               | string of length 1 | 1             |
| b          | signed char        | integer            | 1             |
| B          | unsigned char      | integer            | 1             |
| ?          | _Bool              | bool               | 1             |
| h          | short              | integer            | 2             |
| H          | unsigned short     | integer            | 2             |
| i          | int                | integer            | 4             |
| I(大写的i) | unsigned int       | integer            | 4             |
| l(小写的L) | long               | integer            | 4             |
| L          | unsigned long      | long               | 4             |
| q          | long long          | long               | 8             |
| Q          | unsigned long long | long               | 8             |
| f          | float              | float              | 4             |
| d          | double             | float              | 8             |
| s          | char[]             | string             |
| p          | char[]             | string             |
| P          | void *             | long               |

注- -!
* _Bool在C99中定义,如果没有这个类型,则将这个类型视为char,一个字节;
* q和Q只适用于64位机器;
* 每个格式前可以有一个数字,表示这个类型的个数,如s格式表示一定长度的字符串,4s表示长度为4的字符串;4i表示四个int;
* P用来转换一个指针,其长度和计算机相关;
* f和d的长度和计算机相关;


## 实例
理论性的东西看起来都比较枯燥，来个实例代码就容易理解多了。本例来实现往一个2进制文件中按照某种特定格式写入数据，之后再将它读出。相信通过这个理例子，你就能基本掌握struct的使用。
```python
# -*- coding: utf-8 -*-
__author__ = 'djstava'
 
'''
数据格式为
姓名 年龄 性别   职业
lily 18  female teacher
'''
 
import os
import struct
 
fp = open('test.bin','wb')
 
# 按照上面的格式将数据写入文件中
# 这里如果string类型的话，在pack函数中就需要encode('utf-8')
name = b'lily'
age = 18
sex = b'female'
job = b'teacher'
 
# int类型占4个字节
fp.write(struct.pack('4si6s7s', name,age,sex,job))
fp.flush()
fp.close()
 
# 将文件中写入的数据按照格式读取出来
fd = open('test.bin','rb')
# 21 = 4 + 4 + 6 + 7
print(struct.unpack('4si6s7s',fd.read(21)))
fd.close()
```

```
PS E:\OneDrive\Doc> & C:/ProgramData/Anaconda3/python.exe e:/OneDrive/Doc/MD_Tech/Programming/Python/modules/struct/t.py
(b'lily', 18, b'female', b'teacher')
PS E:\OneDrive\Doc>
```
