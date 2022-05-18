# requests库提示警告InsecureRequestWarning

当使用 requests 库发送请求时报了以下警告
```ps1
D:\python3.6\lib\site-packages\urllib3\connectionpool.py:847: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
  InsecureRequestWarning)
``` 

如何解决
```py
import requests

# 加上这行代码即可，关闭安全请求警告
requests.packages.urllib3.disable_warnings()
```


## ref
* [Python常见问题 - python3 requests库提示警告InsecureRequestWarning的问题 ](https://www.cnblogs.com/poloyy/p/12268671.html)
* []()
* []()
* []()
* []()
* []()
* []()
