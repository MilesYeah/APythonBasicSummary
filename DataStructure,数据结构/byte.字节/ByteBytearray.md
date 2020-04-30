
Python的数据结构（四）bytes和bytearray

## bytes
### bytes的概念
它们俩是python3 中引入的两个新的类型。

bytes 表示字节序列，是一个不可变的数据类型。 
bytearray 表示字节数组，是一个可变的数据类型。

定义这两种类型的数据，在内存中开辟的空间都得是连续的。

听着是很懵逼的，得解释一下：

通常在常用的ASCII、utf-8 和unicode 编码中，像 a 这样一个英文字符，在内存中占一个字节。（一个汉字在ASCII和unicode编码里占两个字节，在utf-8 编码中占三个字节，太麻烦就不说了）

一个字节有八位，也就是八个数字，也叫8个bit 。

计算机中的最小储存单位就是bit，bit是二进制的，所以计算机中的数据全都是0和1，没有其他的数字。

还是以一个字符 a 为例，在ASCII编码表中： 


只要看十进制那列和字符那列就行，别的对于我们理解没什么用。

找到小写字母 a ，它对应的十进制数字是97（十六进制数字就是16），如果转化成二进制数字，就是 0110 0001。

所以这个字符，小写字母 a ， 在内存中的形式就是 0110 0001。但是一定要注意，如果有两个字节在内存中是 0110 0001，它不一定代表的是小写字母 a。因为内存中的0和1填在不同的bit上，形成了一个个位，八个位组成了一个字节，但是不知道这个字节的数据类型，所以不能确定这个字节的意思。况且，就算知道这个字节代表的是字符串类型，如果不知道用的是哪种编码，也是不知道的。

可以看到上面的ASCII码一共有128个，从0000 0000 到0111 1111，正好128个，剩下的128个叫做扩展ASCII 表。

### bytes的相关函数
#### bytes的定义

**bytes()**

定义空字节，空字节前面有个 b 来区分。
```
a = bytes()
a
b''
```

**bytes(int)**

直接定义字节的个数，就是创造了几个空字节，但是每个字节里面是空的。
```
a = bytes(3)
a
b'\x00\x00\x00'
# 这是ASCII 0 ，不是阿拉伯数字0，阿拉伯数字0是十进制48，十六进制30.
```

**bytes(iteratable)**

创造可迭代对象的元素个数相等的字节，然后把每个元素填充进去。 
注意，必须是整型int 的可迭代对象。
```
a = bytes(range(15))
a
b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e'
# 看ASCII表，9 是\t，10是\n，13是\r。这就是用ASCII表来解码的字节。
# 前面那些 00 01 02 03，也有自己的意思，但是没办法用字符表示出来，所以就用它的十六进制表示法表示出来。
```

**bytes(byte) or bytes(‘string’,encode)**

造一个字节序列，还是得用字节。
```
a = bytes(range(3))
a 
b'\x00\x01\x02'

b = a
b
b'\x00\x01\x02'

c = bytes(b'fuck')
```

或者用b前缀，这样也可以，总之里面得是整数，可迭代对象（里面元素为整数），或者是字节类型的。
```
d = bytes('fuck','utf-8')
d
b'fuck'
```


这样定义是，把里面的字符串，用utf-8这种编码来解码返回相应个字节的字节数据。其实返回的不应该是b’fuck’，应该是 \x66\x75\x63\x6b ，这样一串，只不过在ipython等工具中，把它优化成了，便于人类理解的形式。
```
e = b'fuck'
f = b'\x61\x62\x63'
```

不过一般定义字节序列类型的值，都用上面的方法直接定义。

#### bytes的“修改”
bytes 和 str 一样，都是不可修改的类型，所以，所谓的修改，都是创造一个新的 bytes 和 str 。

二者的用法也类似。
```
b'fuck'.replace(b'f',b's')
b'suck'
# 替换字节

b'fuck'.find(b'u')
1
# 查找某个字节的索引号
```

**bytes.fromhex(‘hexstr’)**

这个意思是，用一串由十六进制数字组成的字符串，来表示字节。
```
bytes.fromhex('53 75 63 6b 20 4d 79 20 44 69 63 6b')
b'Suck My Dick'
# 注意，在括号内，空格是无效的，相当于没输入，所以想打出空格，就要打ASCII编码表里空格对应的编码，也就是20。
```


再倒着回来，一个字符串，用encode() 变成字节，然后再用hex() 取它的十六进制表达，得出的和上面输入的是一样的。
```
'Suck My Dick'.encode().hex()
'5375636b204d79204469636b'
```


字节序列，称为序列是有序的，所以也可以用索引
```
'Suck My Dick'.encode()[0]
83
# 这里返回的是十进制的数字，换成十六进制，也就是我们上面输入的S 的编码53。
```

## bytearray
叫做字节数组，是可变的，有序的。

我的理解是，这个bytearray 类型，是好多bytes 组合在一起。

还有一点要注意的是，b前缀，代表的是bytes 类型；而bytearray 类型，表示方法是bytearray(b’ ‘)。

bytearray 类型的操作，和bytes 类型的操作基本差不多。

### bytearray 的定义
* bytearray( ) 
空的字节数组

* bytearray(int) 
创造一个有int个字节的字节数组，所有字节都被十六进制的0x0填充，也就是被null 填充。

* bytearray(interatable_of_int) 
把一个由int 组成的可迭代对象里的元素，依次取出，放在字节数组的字节中。返回值为bytearray(b’ ‘)。

* bytearray(‘string’,encode) 
把字符串string，按encode 指定的编码来解码，然后把解码之后的十六进制数字，放入字节中，组成字节数组。

* bytearray(bytes_or_buffer) 
从一个字节序列或者是buffer中，复制一个新的bytearray，buffer是啥，我暂时还不知道呢，知道了补上。

### bytearray 的修改
用法都和以前一样，就不赘述了。

* bytearray.replace(old,new) 
替换，虽然说bytearray 可变，但是这个替换不是就地修改，返回值是修改之后的，一个新的bytearray 。

* bytearray.find(sub) 
寻找目标的子字节，然后返回索引号。

* bytearray.fromhex(‘string’) 
把一个字符串（这个字符串必须是两个字符的十六进制形式，例如 ‘5375636b204d79204469636b’ ），放在一个bytearray 里。

* bytearray(‘string’,encode()).hex() 
先把一个字符串，以某种编码形式，转换成bytearray 类型的数据，然后再用十六进制表示出来。

* bytearray(bytes)[index] 
返回索引为index 的字节的十进制数字，类型为int。
因为是可变的，所以bytearray 可以就地修改，修改方法和list 的修改方法类似。 

* bytearray.append(int) 
* bytearray.insert(index,int) 
* bytearray.extend(iteratable_of_int) 
* bytearray.pop() 
* bytearray.remove(value) 
* bytearray.clear() 
* bytearray.reverse()

### 整型和字节序列的互相转化
如果无论字符串str 还是整型int ，在内存中都是以字节来储存，那么二者之间可以通过bytes 互相转化。

**int.from_bytes(bytes,byteorder)**
```
int.from_bytes(b'fuck','big')
1718969195
```


以上的意思就是，把字符串 ‘fuck’，通过解码，以整型int（十进制）表示出来。

后面的byteorder 是指大小端模式。

**int.to_bytes(length,byteorder)**

把一个整型的值，转换成字节。
```
1718969195.to_bytes(4,'big')
b'fuck'
```

length 是指定有多少个字符，只能多不能少，多了话，多余的字符会被十六进制的0填充，少了的话会报错。

--------------------- 
作者：LittleHuang950620 
来源：CSDN 
原文：https://blog.csdn.net/LittleHuang950620/article/details/81585294 
版权声明：本文为博主原创文章，转载请附上博文链接！
