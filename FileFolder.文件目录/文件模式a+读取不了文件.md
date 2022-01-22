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




## ref
* [Python常见问题 - 文件模式a+读取不了文件 _](https://www.cnblogs.com/poloyy/p/12353716.html)
* []()
* []()
* []()
* []()
* []()
