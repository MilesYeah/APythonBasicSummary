# requests.异步请求

使用grequests实现异步请求

    urls = [
        'http://www.url1.com',
        'http://www.url2.com',
        'http://www.url3.com',
        'http://www.url4.com',
        'http://www.url5.com',
    ]
    resp = (grequests.get(u) for u in urls)
    grequests.map(resp)



## ref
* [原文链接：](https://blog.csdn.net/weixin_48500307/article/details/108451415)
* []()
* []()
* []()
* []()
* []()
* []()

