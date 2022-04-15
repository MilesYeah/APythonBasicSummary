# Python3之pickle模块
 
## 用于序列化的两个模块
* json：用于字符串和Python数据类型间进行转换
* pickle: 用于python特有的类型和python的数据类型间进行转换
* json提供四个功能：dumps,dump,loads,load
* pickle提供四个功能：dumps,dump,loads,load

## pickle可以存储什么类型的数据呢？
* 所有python支持的原生类型：布尔值，整数，浮点数，复数，字符串，字节，None。
* 由任何原生类型组成的列表，元组，字典和集合。
* 函数，类，类的实例

应用：
``` python
# dumps功能
import pickle
data = ['aa', 'bb', 'cc']  
# dumps 将数据通过特殊的形式转换为只有python语言认识的字符串
p_str = pickle.dumps(data)
print(p_str)            
b'\x80\x03]q\x00(X\x02\x00\x00\x00aaq\x01X\x02\x00\x00\x00bbq\x02X\x02\x00\x00\x00ccq\x03e.

```

``` python
import pickle
# loads功能
# loads  将pickle数据转换为python的数据结构
mes = pickle.loads(p_str)
print(mes)
['aa', 'bb', 'cc']
# dump功能
# dump 将数据通过特殊的形式转换为只有python语言认识的字符串，并写入文件
with open('D:/tmp.pk', 'w') as f:
    pickle.dump(data, f)
# load功能
# load 从数据文件中读取数据，并转换为python的数据结构
with open('D:/tmp.pk', 'r') as f:
    data = pickle.load(f)
```


## pickle模块中常用的函数：
pickle.dump(obj, file, [,protocol])
  * 定义：pickle.dump（对象，文件，[使用协议]）
  * 将要持久化的数据“对象”，保存到“文件”中，使用有3种协议，索引0为ASCII，1为旧式二进制，2为新式二进制协议，不同之处在于2要更高效一些。
  * 默认dump方法使用0做协议

pickle.load(file)
  * 定义：pickle.load(文件)，将file中的对象序列化读出。
  * 从“文件”中读取字符串，将他们反序列化转换为python的数据对象，可以像操作数据类型的这些方法来操作它们　　

pickle.dumps(obj[, protocol])
  * 函数的功能：将obj对象序列化为string形式，而不是存入文件中。
  * obj：想要序列化的obj对象。
  * protocal：如果该项省略，则默认为0。如果为负值或HIGHEST_PROTOCOL，则使用最高的协议版本。

pickle.loads(string)
  * 函数的功能：从string中读出序列化前的obj对象。
  * string：文件名称。

dump() 与 load() 相比 dumps() 和 loads() 还有另一种能力：dump（）函数能一个接一个地将几个对象序列化存储到同一个文件中，随后调用load（）来以同样的顺序反序列化读出这些对象。


