# requests.文件

## 一个请求中发送一个文件

```py
url = 'http://httpbin.org/post'  # 上传文件接口
files = {
    'file': ('test.png',  # 文件名称, 这个是根据标签的name属性的值来设定的，如 name="filename"则字典元素名应为filename
             open('../file/test.png', 'rb'),  # 文件路径
             'image/png',  # 文件类型
             {'Expires': '0'}  # 其他参数,非必传
             )
}  # => 打开上传文件并且加入文件相关参数

data = {
    "name": "test"
}

# data传入请求参数dict,files传入待上传文件参数dict
r = requests.post(url, data=data, files=files)
print(r.json())
```

files字典里的  'file' 键是根据上传组件的name属性来改变的，不一定是file；

返回结果
```sh
C:\Envs\trials\Scripts\python.exe F:/Mirror/SourceCode/trials/rRequests/tRequest/t_post_upload_file.py
{
  "args": {}, 
  "data": "", 
  "files": {
    "file": "data:image/png;base64,iVBORw0KGgoAAAANSUh 这部分是图片的base64编码"
  }, 
  "form": {
    "name": "test"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Content-Length": "6006", 
    "Content-Type": "multipart/form-data; boundary=2f42fd0ce6ded321365bb8475e1d04a9", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.26.0", 
    "X-Amzn-Trace-Id": "Root=1-61960f83-6046097d3d595f3c0a9f9bfd"
  }, 
  "json": null, 
  "origin": "218.13.31.34", 
  "url": "http://httpbin.org/post"
}


Process finished with exit code 0
```

如下HTML代码中上传组件，当你上传一张图片时，抓包可以发现会传两个值，一个是fileField，一个是type，所以你的文件数据dict要包含 fileField 和 type 两个key
```html
<input class="hide" type="file" title="上传头像" name="fileField" id="upload" accept="image/gif,image/jpeg,image/jpg,image/png">
<input class="hide" type="hidden" name="type" value="1">
```
```py
files = {
    'fileField': ('test.png',  # 文件名称
                  open('../file/test.png', 'rb'),  # 文件路径
                  'image/png',  # 文件类型
                  {'Expires': '0'}  # 其他参数,非必传
                  ),
    'type': 1
}  # => 打开上传文件并且加入文件相关参数
```





## 一个请求中发送多个文件

你可以在一个请求中发送多个文件。例如，假设你要上传多个图像文件到一个 HTML 表单，使用一个多文件 field 叫做 "images":

```py
<input type="file" name="images" multiple="true" required="true"/>
```

要实现，只要把文件设到一个元组的列表中，其中元组结构为 (form_field_name, file_info):

```py
import requests

url = 'http://httpbin.org/post'  # 上传文件接口
multiple_files = [
    ('images', ('post_files.png', open('post_files.png', 'rb'), 'image/png')),
    ('images', ('post_files1.png', open('post_files1.png', 'rb'), 'image/png'))
]

# data传入请求参数dict,files传入待上传文件参数dict
r = requests.post(url, files=multiple_files)
print(r.text)
```
```sh
C:\Envs\trials\Scripts\python.exe F:/Mirror/SourceCode/trials/rRequests/tRequest/t_post_upload_multifiles.py
{
  "args": {}, 
  "data": "", 
  "files": {
    "images": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA 图片Base64编码"
  }, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Content-Length": "19130", 
    "Content-Type": "multipart/form-data; boundary=a115bee304aedac0436e3042e89678dc", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.26.0", 
    "X-Amzn-Trace-Id": "Root=1-619611a3-7423817e651e67691b4f34e1"
  }, 
  "json": null, 
  "origin": "218.13.31.34", 
  "url": "http://httpbin.org/post"
}


Process finished with exit code 0

```


我们强烈建议你用二进制模式（binary mode）打开文件。这是因为 requests 可能会为你提供 header 中的 Content-Length，在这种情况下该值会被设为文件的字节数。如果你用文本模式打开文件，就可能碰到错误。





## POST一个多部分编码(Multipart-Encoded)的文件
显式地设置文件名，文件类型和请求头：
```py
import requests

url = 'http://httpbin.org/post'
files = {
    'file': (
        'report_excel.xlsx',       # 文件名
        open('report_excel.xlsx', 'rb'),   # 文件对象
        'application/vnd.ms-excel',     # 文件类型
        {
            'Expires': '0'
        }
    )
}

r = requests.post(url, files=files)
print(r.text)
```

```sh
C:\Envs\trials\Scripts\python.exe F:/Mirror/SourceCode/trials/rRequests/tRequest/t_post_file1.py
{
  "args": {}, 
  "data": "", 
  "files": {
    "file": "data:application/vnd.ms-excel;base64,UEsDBBQABgAIAAAAIQBBN4LP `Excel文件Base64编码`"
  }, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Content-Length": "10088", 
    "Content-Type": "multipart/form-data; boundary=68bd4ced3c44529e37e519ecf8ad9ea5", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.26.0", 
    "X-Amzn-Trace-Id": "Root=1-619613a2-48cfdf807efc02b32a235887"
  }, 
  "json": null, 
  "origin": "218.13.31.34", 
  "url": "http://httpbin.org/post"
}


Process finished with exit code 0
```



### 发送作为文件来接收的字符串：

```py
import requests

url = 'http://httpbin.org/post'
files = {
    'file': (
        'report.csv',
        'some,data,to,send\nanother,row,to,send\n'
    )
}

r = requests.post(url, files=files)
print(r.text)
```

执行结果
```sh
C:\Envs\trials\Scripts\python.exe F:/Mirror/SourceCode/trials/rRequests/tRequest/t_post_file2.py
{
  "args": {}, 
  "data": "", 
  "files": {
    "file": "some,data,to,send\nanother,row,to,send\n"
  }, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Content-Length": "184", 
    "Content-Type": "multipart/form-data; boundary=f577431a286584540a2438da88ba451c", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.26.0", 
    "X-Amzn-Trace-Id": "Root=1-619614bf-6dcba75c4e8510131e2b2284"
  }, 
  "json": null, 
  "origin": "218.13.31.34", 
  "url": "http://httpbin.org/post"
}


Process finished with exit code 0

```




## 流式上传

Requests支持流式上传，这允许你发送大的数据流或文件而无需先把它们读入内存。要使用流式上传，仅需为你的请求体提供一个类文件对象即可：

```py
with open('massive-body') as f:
    requests.post('http://some.url/streamed', data=f)
```

我们强烈建议你用二进制模式（binary mode）打开文件。这是因为 requests 可能会为你提供 header 中的 Content-Length，在这种情况下该值会被设为文件的字节数。如果你用文本模式打开文件，就可能碰到错误。





## 流式下载

极其简单，将二进制格式的响应内容存进本地文件中，根据需要下载的文件的格式来写文件名即可
```py
down_url = 'https://www.imooc.com/mobile/appdown'
res = requests.post(down_url).content
with open("F:/imooc.apk", "wb") as f:
    f.write(res)
```



## 保存文本流

stream 参数
1. False 在大文件传输时使用，文件保存在内存里面，默认值
2. True 内存不够，一般限制文件的大小


```py
>>> r = requests.get('https://api.github.com/events', stream=True)
>>> r.raw
<requests.packages.urllib3.response.HTTPResponse object at 0x101194810>
>>> r.raw.read(10)
'\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x03'
```


```py
with open(filename, 'wb') as fd:
    for chunk in r.iter_content(chunk_size):
        fd.write(chunk)
```






## ref
* [python接口自动化测试 - requests库的post请求进行文件上传 ](https://www.cnblogs.com/poloyy/p/12232541.html)
* []()
* []()
* []()
* []()
* []()
* []()
* []()

