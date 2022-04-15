# 文件模式a+读取不了文件

```py
f = open('test/gbk.txt', 'a+', encoding='utf-8')
print(f.readline())
```

最终的执行结果是输出空，为什么呢？

`a+模式打开文件指针在文件结尾处，所以直接读是读不到内容的`

```py
f = open('test/gbk.txt', 'a+', encoding='utf-8')
print(f.tell())
```

最终输出是28，通常如果要读取完整的文件这个值应该是0开始，这代表文件指针当前所处位置，现在28已经是文件结尾的位置了，所以一个字符都读取不了，那我们要怎么做呢？


```py
f = open('test/gbk.txt', 'a+', encoding='utf-8')
f.seek(0)
print(f.readline())
```

将文件指针重置指向文件头即可！


## eg1
```py
>>> fd=open(r'f:\mypython\test.py','a+')
>>> fd.write('123')
>>> fd.read()
>>> fd.close()
```

close之前，手动打开文件，什么都没写入；close后，手动打开文件，乱码：123嚅?     

原因分析：指针问题。open()以a+模式开启了一个附加读写模式的文件，由于是a，所以指针在文件末尾。此时如果做read()，则Python发现指针位置就是EOF，读取到空字符串。

在写入123之后，指针的位置是4，仍然是文件尾，文件在内存中是123[EOF]。

但看起来read()的时候，Python仍然去试图在磁盘的文件上，将指针从文件头向后跳3，再去读取到EOF为止。

也就是说，你实际上是跳过了该文件真正的EOF，为硬盘底层的数据做了一个dump，一直dump到了一个从前存盘文件的[EOF]为止。所以最后得到了一些根本不期待的随机乱字符，而不是编码问题造成的乱码。

解决方案：读取之前将指针重置为文件头（如果读取之后重置再读，无效）

```py
>>> fd=open(r'f:\mypython\test.py','a+')
>>> fd.seek(0)
>>> fd.read()
'123'<span style="white-space:pre">			</span>#顺利读出</span></span>
```

## ref
* [Python常见问题 - 文件模式a+读取不了文件 _](https://www.cnblogs.com/poloyy/p/12353716.html)
* [【Python】python文件打开方式详解——a、a+、r+、w+、rb、rt区别](https://bluebird.blog.csdn.net/article/details/47259805?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ETopBlog-1.topblog&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ETopBlog-1.topblog&utm_relevant_index=1)
* []()
* []()
* []()
* []()
