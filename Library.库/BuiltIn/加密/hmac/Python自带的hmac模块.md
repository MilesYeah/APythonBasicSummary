[Python自带的hmac模块实现了标准的Hmac算法](https://www.cnblogs.com/ncuhwxiong/p/8124940.html)


我们首先需要准备待计算的原始消息message，随机key，哈希算法，这里采用MD5，使用hmac的代码如下：

```py
import hmac
message = b'Hello world'
key = b'secret'
h = hmac.new(key,message,digestmod='MD5')
print(h.hexdigest())

```
可见使用hmac和普通hash算法非常类似。hmac输出的长度和原始哈希算法的长度一致。需要注意传入的key和message都是bytes类型，str类型需要首先编码为bytes。



```py
def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.key, password)
```



