

## 超时（timeout）

你可以告诉 requests 在经过以 timeout 参数设定的秒数时间之后停止等待响应。基本上所有的生产代码都应该使用这一参数。如果不使用，你的程序可能会永远失去响应：
```py
>>> requests.get('http://github.com', timeout=0.001)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
requests.exceptions.Timeout: HTTPConnectionPool(host='github.com', port=80): Request timed out. (timeout=0.001)
```

timeout 仅对连接过程有效，与响应体的下载无关。 
timeout 并不是整个下载响应的时间限制，而是如果服务器在 timeout 秒内没有应答，将会引发一个异常
（更精确地说，是在 timeout 秒内没有从基础套接字上接收到任何字节的数据时）
If no timeout is specified explicitly, requests do not time out.



为防止服务器不能及时响应，大部分发至外部服务器的请求都应该带着 timeout 参数。在默认情况下，除非显式指定了 timeout 值，requests 是不会自动进行超时处理的。如果没有 timeout，你的代码可能会挂起若干分钟甚至更长时间。

连接超时指的是在你的客户端实现到远端机器端口的连接时（对应的是`connect()`_），Request 会等待的秒数。一个很好的实践方法是把连接超时设为比 3 的倍数略大的一个数值，因为 TCP 数据包重传窗口 (TCP packet retransmission window) 的默认大小是 3。

一旦你的客户端连接到了服务器并且发送了 HTTP 请求，读取超时指的就是客户端等待服务器发送请求的时间。（特定地，它指的是客户端要等待服务器发送字节之间的时间。在 99.9% 的情况下这指的是服务器发送第一个字节之前的时间）。

如果你制订了一个单一的值作为 timeout，如下所示：
```py
r = requests.get('https://github.com', timeout=5)
```

这一 timeout 值将会用作 connect 和 read 二者的 timeout。如果要分别制定，就传入一个元组：
```py
r = requests.get('https://github.com', timeout=(3.05, 27))
```

如果远端服务器很慢，你可以让 Request 永远等待，传入一个 None 作为 timeout 值，然后就冲咖啡去吧。
```py
r = requests.get('https://github.com', timeout=None)
```






## 错误与异常
遇到网络问题（如：DNS 查询失败、拒绝连接等）时，Requests 会抛出一个 ConnectionError 异常。

如果 HTTP 请求返回了不成功的状态码， Response.raise_for_status() 会抛出一个 HTTPError 异常。

若请求超时，则抛出一个 Timeout 异常。

若请求超过了设定的最大重定向次数，则会抛出一个 TooManyRedirects 异常。

所有Requests显式抛出的异常都继承自 requests.exceptions.RequestException 。





