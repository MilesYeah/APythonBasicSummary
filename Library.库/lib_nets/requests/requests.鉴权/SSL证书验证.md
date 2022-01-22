# SSL证书验证

`requests.exceptions.SSLError` `certificate verify failed`

当发送请求如果报以上错误时，可以在请求方法里加多一个字段 verify=False ，就可以解决此问题；此操作是为了免去验证步骤

```py
url = 'https://www.imooc.com'
res = requests.get(url, verify=False)
```



## 消除警告信息
```py
# 请求https的网站忽略SSL证书验证之后还是会出现警告信息，在请求前加上下面这句就可以禁用安全请求警告
# InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings InsecureRequestWarning）
requests.packages.urllib3.disable_warnings()
```
