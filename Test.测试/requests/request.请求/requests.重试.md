# requests.重试

requests请求失败后，增加重试机制(若失败，将会重试3次)

```py
request_retry = requests.adapatrs.HTTPAdapaters(max_retries=3）
session.mount('https://',request_retry)
```

