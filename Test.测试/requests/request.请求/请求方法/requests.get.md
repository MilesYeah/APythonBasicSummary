# request.get

## 发送请求

```py
>>> import requests
>>> url = 'https://www.baidu.com/'
>>> r = requests.get(url)
>>> r.status_code
200
>>> r.headers['content-type']
'text/html'
>>> r.encoding
'ISO-8859-1'
>>> 
>>> r.text
'<!DOCTYPE html>\r\n<!--STATUS OK--><html> ...
>>>
```



## params： GET 传递 URL 参数
```py
>>> payload = {'key1': 'value1', 'key2': 'value2'}
>>> r = requests.get("http://httpbin.org/get", params=payload)

>>> payload = {'key1': 'value1', 'key2': ['value2', 'value3']}

>>> r = requests.get('http://httpbin.org/get', params=payload)
>>> print(r.url)
http://httpbin.org/get?key1=value1&key2=value2&key2=value3
```


