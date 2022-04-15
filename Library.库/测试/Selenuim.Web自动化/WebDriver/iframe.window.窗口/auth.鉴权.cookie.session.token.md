# auth.鉴权.cookie.session.token

网站为了辨别用户身份、进行 session 跟踪而存储在用户本地终端上的数据，也可以叫做浏览器缓存。webdriver 对 cookie 的常用操作有添加、删除、读取。

有时候我们需要验证浏览器中Cookie是否正确，因为基于真实Cookie的测试是无法通过白盒和集成测试进行的

测试某些网站若需要先登录，可以直接通过接口去登录，把返回的Cookie存起来，相当于UI自动化上的免登录了，除开了不必要的登录操作

| 方法                                      | 描述                                                            |
| ----------------------------------------- | --------------------------------------------------------------- |
| driver.get_cookies()                      | 获得所有的 cookie 信息                                          |
| driver.get_cookie(name)                   | 获得 key 值为 name 的 cookie 的信息                             |
| driver.add_cookie(cookie_dict)            | 添加 cookie。"cookie_dict" 指字典对象，必须有 name 和 value 值  |
| driver.delete_cookie(name, optionsString) | 删除cookie信息。                                                |
|                                           | “name”是要删除的cookie的名称，                                  |
|                                           | “optionsString”是该cookie的选项，目前支持的选项包括“路径”，“域” |
| driver.delete_all_cookies()               | 删除所有 cookie 信息                                            |
|                                           |                                                                 |
|                                           |                                                                 |

1. get_cookie：从get_cookies()返回的Cookie列表中，循环判断，获取对应的Cookie
2. add_cookie：传入dict对象，有两个必传key值：name、vlaue；五个可选key值：path、domain、secure、expiry、httpOnly；可以看到你的字典对象不能乱传key，否则会报错
3. delete_cookie：传入的是Cookie的name值



## cookie 通过 requests 和 selenium 读取的差异

```py
#这里需要注意区别，按住格式进行转换
#request 请求返回cookie的格式
{'PHPSESSID': 'alvrh1i2h7joj2il2jn3sh7up1', 'uid': '16'}

#selenium方法需要的cookie的格式
{'value': 'alvrh1i2h7joj2il2jn3sh7up1', 'httpOnly': False, 'domain': 'yingxiao.chewumi.com', 'name': 'PHPSESSID', 'secure': False, 'path': '/'}
```




## 实例
```py
# 浏览器
driver = webdriver.Chrome()
driver.get("https://px.seewo.com/product")

# 获得网站的Cookies信息
cookie = driver.get_cookies()

# 将获得Cookies的信息打印
print(cookie)

# 发起登录请求

# 登录后存放的两个token，需要添加到Cookie中去
cookie_list = {}
cookies["px-token"] = exchangedToken
cookies["x-token"] = token

# 添加Cookie
for cookie_ in cookies.items():
    driver.add_cookie({'name': cookie_[0], 'value': cookie_[1], 'path': '/', 'httpOnly': True, 'secure': True})

# 再次打印Cookie
print(driver.get_cookies())

# 执行UI自动化操作
# ......
# ......

# 发起退出登录请求

# 删除某个Cookie
driver.delete_cookie("x-token")

# 删除所有Cookie
driver.delete_all_cookies()

# 浏览器关闭
driver.quit()
```



## eg
首先利用request模块，请求登陆地址进行登陆，登陆成功以后获取cookie值，然后再通过add_cookie添加到浏览器，使系统处于登陆状态。

需要注意的是request请求返回的cookie的格式不能直接传入add_cookie方法，所以这里需要进行转换。

```py
#-*- coding:utf-8 -*-
import time
import requests
from selenium import webdriver

def get_system_cookies(url,account,password):
    '''通过request 登陆系统，获取cookie'''
    cookiesList = []
    data = {"username":account,"passwd":password}
    roomSession  = requests.Session()
    roomSession.post(url,data=data)
    loadCookies = requests.utils.dict_from_cookiejar(roomSession.cookies)
    for cookieName,cookieValue in loadCookies.items():
        cookies = {}
        cookies['name'] = cookieName
        cookies['value'] = cookieValue
        cookiesList.append(cookies)
    return cookiesList

def is_login_status_succeed(driver):
    '''判断是否登陆状态，非登陆状态,通过cookie登陆'''
    loginUrl = 'http://yingxiao.chewumi.com/login.php'  #登陆地址
    account = 'account'  #账号
    password = 'password'  #密码
    driver.get('http://yingxiao.chewumi.com/index.php') #测试是否为登陆状态
    if '请登录' in driver.page_source:  #判断是否登陆为登陆页面
        for cookie in get_system_cookies(loginUrl,account,password): #如果登陆界面获取cookie
            driver.add_cookie(cookie)  #添加cookie ，通过Cookie登陆
    return driver

def request_circle_details(driver,requestUrl):
    '''测试跳转圈子详情'''
    is_login_status_succeed(driver)
    driver.get(requestUrl)
    verifyField = driver.find_element_by_xpath('/html/body/div/div/div[2]/h1').text  #获取页面标题
    try:
        assert verifyField == '圈子详情'
        return '测试通过'
    except AssertionError as e:
        return '测试未通过'


'''测试下效果'''
requestUrl = 'http://yingxiao.chewumi.com/list.php?page=1'
driver = webdriver.Chrome()
driver.maximize_window()
print (request_circle_details(driver,requestUrl))
driver.get(requestUrl)
time.sleep(2)
driver.quit()
```


## eg


```py
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Time    :   2020/4/15
@Author  :   公众号：软测之家  更多技术干货，软测视频，面试资料请关注！
@Contact :   软件测试技术群：695458161
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""
from selenium import webdriver
from time import sleep
    
    
base_url = 'https://www.baidu.com/'
browser = webdriver.Chrome('../tools/chromedriver.exe')
browser.get(base_url)
    
# 1. 获取 cookie 信息
cookies = browser.get_cookies()
print(cookies)
sleep(2)
browser.quit()
    
# 2. cookie 写入
browser.add_cookie(
    {
        'name': 'add-cookie',
        'value': 'add-cookie-value'
    }
)
# 遍历cookies打印cookie信息
for cookie in browser.get_cookies():
    print("%s ---> %s" % (cookie['name'], cookie['value']))
sleep(2)
browser.quit()
```





## ref
* [python和selenium实现Web自动化(4)：文件上传，Cookie操作，调用 JavaScript，窗口截图](https://blog.csdn.net/weixin_48500307/article/details/108450895)
* [Selenium系列（21） - Cookie操作和源码解读 _](https://www.cnblogs.com/poloyy/p/12640783.html)
* [python selenium-webdriver 通过cookie登陆（十一）](https://www.cnblogs.com/mengyu/p/7078561.html)
* []()
* []()
* []()
* []()

