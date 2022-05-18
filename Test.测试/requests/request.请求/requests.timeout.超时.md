# requests.timeout.超时





可以利用 timeout 变量来配置最大请求时间
```py
>>> import requests
>>> a = requests.get("https://www.baidu.com/", timeout=3)
>>> a.status_code
200
>>>
```

注：timeout 仅对连接过程有效，与响应体的下载无关。

也就是说，这个时间只限制请求的时间。即使返回的 response 包含很大内容，下载需要一定时间。



