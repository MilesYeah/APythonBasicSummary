# 字符串的rbfu

## 字符串前加 f（重点！敲黑板！）

作用：相当于 format() 函数
```py
name = "帅哥"
age = 12
print(f"my name is {name},age is {age}")
```
执行结果
```
my name is 帅哥,age is 12
```
 
## 字符串前加 r

r""  的作用是：去除转义字符

场景：想复制某个文件夹的目录，假设是 F:\Python_Easy\n4\test.py 

当你不用 r"" ，你有三种写法
```py
print("F:\Python_Easy\n4\test.py ")
print("F:\\Python_Easy\\n4\\test.py ")
print("F:/Python_Easy/n4/test.py ")
```
而通常如果直接复制目录路径的话，你就粘贴出来的字符串就是第一行代码所示，所有 \ 会当成转义符；而为了消除转义作用，需要手动再加一个 \ ，否则你也得手动改成第三行代码一样
执行结果
```
F:\Python_Easy
4    est.py 
F:\Python_Easy\n4\test.py 
F:/Python_Easy/n4/test.py 
```
而 r"" 的出现就是为了避免这种情况，如下：
```py
print(r"F:\Python_Easy\n4\test.py ")
```
执行结果
```
F:\Python_Easy\n4\test.py 
```
 
## 字符串前加 b

b" "的作用是：后面字符串是bytes 类型

话不多说，直接上代码
```py
print("中文".encode(encoding="utf-8"))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode())
print(r'\xe4\xb8\xad\xe6\x96\x87')
```
执行结果
```
b'\xe4\xb8\xad\xe6\x96\x87'
中文
\xe4\xb8\xad\xe6\x96\x87
```
可以看到，当你不加 b"" 时，他也就是个普通的字符串而已，不会识别为字节类型

bytes应用场景：像图片、音视频等文件的读写就是用bytes数据

 

顺便可以看看字符串和bytes之间的转换是怎么样的：https://www.cnblogs.com/poloyy/p/12341746.html

 
## 字符串前加 u

作用：后面字符串以 Unicode 格式 进行编码

实际场景：一般用在中文字符串前面，防止因为源码储存格式问题，导致再次使用时出现乱码。

建议所有编码方式采用utf8

 


## ref
* [ Python - r'', b'', u'', f'' 的含义 _ ](https://www.cnblogs.com/poloyy/p/12444579.html)
* []()
* []()
* []()
* []()

