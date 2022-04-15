# request.post



## data传递form表单： POST 传递数据 更加复杂的 POST 请求

```py
import requests

url = 'http://httpbin.org/post'
data = {
    'name': 'jack',
    'age': '23'
}
response = requests.post(url, data=data)
print(response.text)

```

可以从返回内容中看出，传递进去的data都存储在form表单中。
```py
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "age": "23", 
    "name": "jack"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Content-Length": "16", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.26.0", 
    "X-Amzn-Trace-Id": "Root=1-619609b5-68fe60c0393c9edc1cee7a95"
  }, 
  "json": null, 
  "origin": "218.13.31.34", 
  "url": "http://httpbin.org/post"
}

```

## json传递form表单： POST 传递数据 更加复杂的 POST 请求

```py
>>> import json

>>> url = 'https://api.github.com/some/endpoint'
>>> payload = {'some': 'data'}

>>> r = requests.post(url, data=json.dumps(payload))

>>> url = 'https://api.github.com/some/endpoint'
>>> payload = {'some': 'data'}

>>> r = requests.post(url, json=payload)
```


### 从字典参数中移除一个值
有时你会想省略字典参数中一些会话层的键。要做到这一点，你只需简单地在方法层参数中将那个键的值设置为 None ，那个键就会被自动省略掉。

