# requests发送HTTPS请求报certificate verify failed

当你使用 requests 发送HTTPS请求时
```py
requests.get(url, parmas=parmas, headers=header, cookies=cookie) 
```
出现了以下错误
```
HTTPSConnectionPool(host='www.imooc.com', port=443): Max retries exceeded with url: /api3/getbanneradvertver2 (Caused by SSLError(SSLError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:847)'),))
``` 

出现原因
当你发送HTTPS请求时，需要SSL验证，而requests请求方法的 verify 参数默认是 True ，表示要进行验证

 

如何解决？
关掉验证即可，如下
```py
requests.get(url, parmas=parmas, headers=header, cookies=cookie, verify=False) 
```
 


 ## ref
* [Python常见问题 - python3 使用requests发送HTTPS请求报certificate verify failed 错误 ](https://www.cnblogs.com/poloyy/p/12268701.html)
* []()
* []()
* []()
* []()
* []()
* []()
* []()
