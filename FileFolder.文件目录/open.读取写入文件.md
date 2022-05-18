# open 读取写入文件




## mode



### 换行符

关于换行符的识别问题，在Unix和Windows中是不一样的(分别是 \n 和 \r\n )。 默认情况下，Python会以统一模式处理换行符。 这种模式下，在读取文本的时候，Python可以识别所有的普通换行符并将其转换为单个 \n 字符。 类似的，在输出时会将换行符 \n 转换为系统默认的换行符。 如果你不希望这种默认的处理方式，可以给 open() 函数传入参数 newline='' ，就像下面这样：
```py
# Read with disabled newline translation
with open('somefile.txt', 'rt', newline='') as f:
    ...
```

为了说明两者之间的差异，下面我在Unix机器上面读取一个Windows上面的文本文件，里面的内容是 hello world!\r\n ：
```py
>>> # Newline translation enabled (the default)
>>> f = open('hello.txt', 'rt')
>>> f.read()
'hello world!\n'

>>> # Newline translation disabled
>>> g = open('hello.txt', 'rt', newline='')
>>> g.read()
'hello world!\r\n'
>>>
```




## encodong

Python支持非常多的文本编码。几个常见的编码是ascii, latin-1, utf-8和utf-16。 
* 在web应用程序中通常都使用的是UTF-8。 
* ascii对应从U+0000到U+007F范围内的7位字符。 
* latin-1是字节0-255到U+0000至U+00FF范围内Unicode字符的直接映射。 
  * 当读取一个未知编码的文本时使用latin-1编码永远不会产生解码错误。 
  * 使用latin-1编码读取一个文件的时候也许不能产生完全正确的文本解码数据， 但是它也能从中提取出足够多的有用数据。
  * 同时，如果你之后将数据回写回去，原先的数据还是会保留的。





## errors

可以给 open() 函数传递一个可选的 errors 参数来处理编码错误
* errors='replace'
* errors='ignore'

如果你经常使用 errors 参数来处理编码错误，可能会让你的生活变得很糟糕。 
对于文本处理的首要原则是确保你总是使用的是正确编码。当模棱两可的时候，就使用默认的设置(通常都是UTF-8)。




## ref
* [5.1 读写文本数据](https://python3-cookbook.readthedocs.io/zh_CN/latest/c05/p01_read_write_text_data.html)
* []()
* []()
* []()
* []()
* []()
* []()
* []()
* []()

