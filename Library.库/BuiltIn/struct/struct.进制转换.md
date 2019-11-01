# [python之struct详解](https://blog.csdn.net/qq_30638831/article/details/80421019)

## 进制转化:

获取用户输入十进制数
```python
dec = int(input("输入数字："))

print("十进制数为：", dec)
print("转换为二进制为：", bin(dec))
print("转换为八进制为：", oct(dec))
print("转换为十六进制为：", hex(dec))
```

* 16进制转10进制: int('0x10', 16)  ==>  16

Python没有专门处理字节的数据类型。但由于b'str'可以表示字节，所以，字节数组＝二进制str。而在C语言中，我们可以很方便地用struct、union来处理字节，以及字节和int，float的转换。

在Python中，比方说要把一个32位无符号整数变成字节，也就是4个长度的bytes，你得配合位运算符这么写：

```
>>> n = 10240099
>>> hex(n)
'0x9c4063'
>>> n & 0xff000000
0
>>> n & 0xff000000 >> 24
99
>>> (n & 0xff000000) >> 24
0
>>> n & 0xff0000
10223616
>>> (n & 0xff0000) >> 16
156
>>> n & 0x000000
0
>>> n & 0xf00000
9437184
>>> n & 0xff0000
10223616
>>> 12 * 16**4 + 9 * 16**5
10223616
>>> n & 0xff00
16384
>>> (n & 0xff00) >> 8
64
>>> n & 0xff
99
>>>
```

```python
>>> n = 10240099
>>> b1 = (n & 0xff000000) >> 24
>>> b2 = (n & 0xff0000) >> 16
>>> b3 = (n & 0xff00) >> 8
>>> b4 = n & 0xff
>>> bs = bytes([b1, b2, b3, b4])
>>> bs
b'\x00\x9c@c'
```


非常麻烦。如果换成浮点数就无能为力了。

好在Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换。

struct的pack函数把任意数据类型变成bytes：
```
>>> import struct
>>> struct.pack('>I', 10240099)
b'\x00\x9c@c'
```

pack的第一个参数是处理指令，'>I'的意思是：

>表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。

后面的参数个数要和处理指令一致。

```
>>> import struct
>>> struct.unpack('>I', b'\x00\x9c@c')
(10240099,)
>>>
```
