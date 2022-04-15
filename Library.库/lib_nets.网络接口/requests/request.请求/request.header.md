# request.header



## 请求头
然而，如果想得到发送到服务器的请求的头部，我们可以简单地访问该请求，然后是该请求的头部：
```py
>>> r.request.headers
{'Accept-Encoding': 'identity, deflate, compress, gzip',
'Accept': '*/*', 'User-Agent': 'python-requests/0.13.1'}
```




## 添加header
首先说，为什么要加header（头部信息）呢？例如下面，我们试图访问知乎的登录页面（当然大家都你要是不登录知乎，就看不到里面的内容），我们试试不加header信息会报什么错。

```py
import requests

url = 'https://www.zhihu.com/'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0"
}

r1 = requests.get(url, verify=False)
print(r1.text)

print("----------------------------------------------------------------------------------")
r2 = requests.get(url, verify=False, headers=headers)
print(r2.text)
```

结果：提示发生内部服务器错误（也就说你连知乎登录页面的html都下载不下来）。
```html
<body bgcolor="white">
<center><h1>403 Forbidden</h1></center>
<hr><center>openresty</center>
</body>
```



如果想访问就必须得加headers信息。如上述代码中需要添加一个 headers 字典

```sh
C:\Envs\trials\Scripts\python.exe F:/Mirror/SourceCode/trials/rRequests/tRequest/t_header_add.py
C:\Envs\trials\lib\site-packages\urllib3\connectionpool.py:1013: InsecureRequestWarning: Unverified HTTPS request is being made to host 'www.zhihu.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
  warnings.warn(
<html>
<head><title>403 Forbidden</title></head>
<body bgcolor="white">
<center><h1>403 Forbidden</h1></center>
<hr><center>openresty</center>
</body>
</html>

----------------------------------------------------------------------------------
C:\Envs\trials\lib\site-packages\urllib3\connectionpool.py:1013: InsecureRequestWarning: Unverified HTTPS request is being made to host 'www.zhihu.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
  warnings.warn(
C:\Envs\trials\lib\site-packages\urllib3\connectionpool.py:1013: InsecureRequestWarning: Unverified HTTPS request is being made to host 'www.zhihu.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/1.26.x/advanced-usage.html#ssl-warnings
  warnings.warn(
<!doctype html>
<html lang="zh" data-theme="light"><head><meta charSet="utf-8"/><title data-react-helmet="true">知乎 - 有问题，就会有答案</title><meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1"/><meta name="renderer" content="webkit"/><meta name="force-rendering" content="webkit"/><meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/><meta name="google-site-verification" content="FTeR0c8arOPKh8c5DYh_9uu98_zJbaWw53J-Sch9MTg"/><meta name="description" property="og:description" content="知乎，中文互联网高质量的问答社区和创作者聚集的原创内容平台，于 2011 年 1 月正式上线，以「让人们更好地分享知识、经验和见解，找到自己的解答」为品牌使命。知乎凭借认真、专业、友善的社区氛围、独特的产品机制以及结构化和易获得的优质内容，聚集了中文互联网科技、商业、影视、时尚、文化等领域最具创造力的人群，已成为综合性、全品类、在诸多领域具有关键影响力的知识分享社区和创作者聚集的原创内容平台，建立起了以社区驱动的内容变现商业模式。"/><link data-react-helmet="true" rel="apple-touch-icon" href="https://static.zhihu.com/heifetz/assets/apple-touch-icon-152.a53ae37b.png"/><link data-react-helmet="true" rel="apple-touch-icon" href="https://static.zhihu.com/heifetz/assets/apple-touch-icon-152.a53ae37b.png" sizes="152x152"/><link data-react-helmet="true" rel="apple-touch-icon" href="https://static.zhihu.com/heifetz/assets/apple-touch-icon-120.bbce8f18.png" sizes="120x120"/><link data-react-helmet="true" rel="apple-touch-icon" href="https://static.zhihu.com/heifetz/assets/apple-touch-icon-76.cbade8f9.png" sizes="76x76"/><link data-react-helmet="true" rel="apple-touch-icon" href="https://static.zhihu.com/heifetz/assets/apple-touch-icon-60.8f6c52aa.png" sizes="60x60"/><link crossorigin="" rel="shortcut icon" type="image/x-icon" href="https://static.zhihu.com/heifetz/favicon.ico"/><link crossorigin="" rel="search" type="application/opensearchdescription+xml" href="https://static.zhihu.com/heifetz/search.xml" title="知乎"/><link rel="dns-prefetch" href="//static.zhimg.com"/><link rel="dns-prefetch" href="//pic1.zhimg.com"/><link rel="dns-prefetch" href="//pic2.zhimg.com"/><link rel="dns-prefetch" href="//pic3.zhimg.com"/><link rel="dns-prefetch" href="//pic4.zhimg.com"/><style>
.u-safeAreaInset-top {
  height: constant(safe-area-inset-top) !important;
  height: env(safe-area-inset-top) !important;
  
}
.u-safeAreaInset-bottom {
  height: constant(safe-area-inset-bottom) !important;
  height: env(safe-area-inset-bottom) !important;
  
}
</style><link href="https://static.zhihu.com/heifetz/main.app.216a26f4.f645af476dbe5a506486.css" crossorigin="" rel="stylesheet"/><link href="https://static.zhihu.com/heifetz/main.sign-page.216a26f4.842ddf25986733b9d1ee.css" crossorigin="" rel="stylesheet"/><script nonce="94318da2-b11b-4dfd-813f-f0f6037ca646">!function(){"use strict";!function(e,n){var r=[];function t(e){return function(){r.push([e,arguments])}}n.Raven={captureException:t("captureException"),captureMessage:t("captureMessage"),captureBreadcrumb:t("captureBreadcrumb")};var a,o,c,i,s,u="undefined"!=typeof DOMError;function d(e){var n=e instanceof Error||e instanceof ErrorEvent||u&&e instanceof DOMError||e instanceof DOMException;Raven.captureException(n?e:new Error(e.message||e.reason))}n.addEventListener("unhandledrejection",d),n.addEventListener("error",d,!0),a=e.src,o=e,c=function(){r.forEach(function(e){var n;(n=Raven)[e[0]].apply(n,e[1])}),n.removeEventListener("unhandledrejection",d),n.removeEventListener("error",d,!0)},i=document.head||document.getElementsByTagName("head")[0],(s=document.createElement("script")).crossOrigin=o.crossOrigin,s.dataset.sentryConfig=o["data-sentry-config"],s.onload=c,s.src=a,i.appendChild(s)}({"defer":true,"crossOrigin":"anonymous","src":"https://unpkg.zhimg.com/@cfe/sentry-script@1.3.0/dist/init.js","data-sentry-config":"{\"dsn\":\"https://2d8d764432cc4f6fb3bc78ab9528299d@crash2.zhihu.com/1224\",\"sampleRate\":0.1,\"release\":\"3343-812009f1\",\"ignoreErrorNames\":[\"NetworkError\",\"SecurityError\"],\"ignoreErrorsPreset\":\"ReactApp\"}"},window)}();
</script></head><body>.........HTML_CONTENT.............</script></html>

Process finished with exit code 0
```



## 请求的对象类型导致请求出错

在使用requests去请求一个接口时，出现报错的情况，但是这个接口本身却没有问题。这是因为接口的请求参数有两种情况：简单类型(一般少于3个）和复杂对象类型。

解决方法：在headers中定义一下这两种参数的类型
* 简单类型：
  * `headers={"Content-Type": "application/x-www-form-urlencoded"}`
* 复杂对象类型：
  * `headers={"Content-Type":application/json}`




## ref
* [原文链接：](https://blog.csdn.net/weixin_48500307/article/details/108451415)
* []()
* []()
* []()
* []()
* []()
* []()
* []()
* []()
* []()
