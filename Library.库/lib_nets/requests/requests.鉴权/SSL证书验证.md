# SSL证书验证

`requests.exceptions.SSLError` `certificate verify failed`

当发送请求如果报以上错误时，可以在请求方法里加多一个字段 verify=False ，就可以解决此问题；此操作是为了免去验证步骤

```py
url = 'https://www.imooc.com'
res = requests.get(url, verify=False)
```
