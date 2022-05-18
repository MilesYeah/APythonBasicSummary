# Http 代理

代理服务器充当客户端和服务器之间的请求中介. 简述而言, 流量将通过代理服务器流向您请求的地址, 然后返回.

使用代理服务器用于Selenium的自动化脚本, 可能对以下方面有益:
* 捕获网络流量
* 模拟网站后端响应
* 在复杂的网络拓扑结构或严格的公司限制/政策下访问目标站点.

如果您在公司环境中, 并且浏览器无法连接到URL, 则最有可能是因为环境, 需要借助代理进行访问.

Selenium WebDriver提供了如下设置代理的方法

```py
from selenium import webdriver

PROXY = "<HOST:PORT>"
webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,
    "proxyType": "MANUAL",

}

with webdriver.Firefox() as driver:
    # Open URL
    driver.get("https://selenium.dev")
```






## 示例

```py
import time 
from selenium.webdriver.common.proxy import*

myProxy = '202.202.90.20:8080'

proxy = Proxy({
    'proxyType': ProxyType.MANUAL, 
    'httpProxy': myProxy, 
    'ftpProxy': myProxy, 
    'sslProxy': myProxy, 
    'noProxy': ''
})

profile = webdriver.FirefoxProfile()
if proxy:
    profile = get_firefox_profile_with_proxy_set(profile, proxy)
if user_agent:
    profile.set_preference("general.useragent.override", user_agent)

driver=webdriver.Firefox(proxy=proxy,profile=profile) 
driver.get('https://www.baidu.com') 
time.sleep(3) 
driver.quit()
```


## 设置代理请求头
```py
import time 
from selenium import webdriver
from selenium.webdriver.common.proxy import * 

myProxy = '202.202.90.20:8080'

# 用于快速设置 profile 的代理信息的方法
def get_firefox_profile_with_proxy_set(profile, proxy_host):
    # proxy_host
    proxy_list = proxy_host.split(':')
    agent_ip = proxy_list[0]
    agent_port = proxy_list[1]

    profile.set_preference('network.proxy.type', 1)  # 使用代理
    profile.set_preference('network.proxy.share_proxy_settings', True)  # 所有协议公用一种代理配置
    profile.set_preference('network.proxy.http', agent_ip)
    profile.set_preference('network.proxy.http_port', int(agent_port))
    profile.set_preference('network.proxy.ssl', agent_ip)
    profile.set_preference('network.proxy.ssl_port', int(agent_port))
    # 对于localhost的不用代理，这里必须要配置，否则无法和 webdriver 通讯
    profile.set_preference('network.proxy.no_proxies_on', 'localhost,127.0.0.1')
    profile.set_preference('network.http.use-cache', False)

    return profile

profile = webdriver.FirefoxProfile()
if proxy:
    profile = get_firefox_profile_with_proxy_set(profile, myProxy)
if user_agent:
    profile.set_preference("general.useragent.override", user_agent)

driver=webdriver.Firefox(profile=profile) 
driver.get('https://www.baidu.com') 
time.sleep(3) 
driver.quit()
```


## firefox无头模式
```py
from selenium import webdriver

# 创建的新实例驱动
options = webdriver.FirefoxOptions()
#火狐无头模式
options.add_argument('--headless')
options.add_argument('--disable-gpu')
# options.add_argument('window-size=1200x600')

executable_path='./source/geckodriver/geckodriver.exe'
driver_path = webdriver.Firefox(firefox_options=options,executable_path=executable_path)
```

## Firefox设置代理(认证)
熟悉Firefox的同学都知道，Firefox在配置HTTP代理时无法设置用户名和密码。而收费的HTTP代理大多都是需要进行用户名和密码认证的（有的也支持IP白名单，但前提是你的IP需要固定不变）。这就使得使用Selenium + Firefox进行自动化操作非常不方便，因为每次启动一个新的浏览器实例就会弹出一个授权验证窗口，被要求输入用户名和密码，打断了自动化操作流程。


另外，Firefox也没有提供设置用户名密码的命令行参数（PS：phantomjs就有–proxy-auth这样的参数）。难道真的没有解决方法了？

鲲之鹏的技术人员通过研究终于找到了一个有效并且稳定的解决方案：

先介绍一个重要的角色，它的主页是https://addons.mozilla.org/en-US/firefox/addon/close-proxy-authentication/。close-proxy-authentication实现了自动完成代理用户名密码认证（Proxy Authentication）的功能，它提供了一个extensions.closeproxyauth.authtoken参数用来设置代理的用户名和密码，其值为经过base64编码后的用户名密码对（如下图所示)。close-proxy-authentication会使用该值构造出"Proxy-Authorization: Basic dGVzdDp0ZXN0"头发给代理服务器，以通过认证，这就是它的工作原理。

我们就是要借助这个插件在Selenium + Firefox时自动完成HTTP代理认证，流程是这样的：

1. 通过Firefox配置选项动态添加close-proxy-authentication这个插件（默认不加载任何插件）；
2. 通过配置选项设置HTTP代理的IP和端口参数；
3. 设置extensions.closeproxyauth.authtoken的值为base64encode(“用户名:密码”)；
4. 后续访问网站的时候close-proxy-authentication插件将自动完成代理的授权验证过程，不会再弹出认证窗口；

上述环境涉及文件打包下载地址：http://pan.webscraping.cn:8000/index.php/s/PMDjc77gbCFJzpO

需要特别注意的是：
1. close-proxy-authentication的最新版本目前是V1.1，它并不兼容最新版的Firefox，鲲之鹏的技术人员测试发现Firefox V56.0以下版本能够兼容close-proxy-authentication V1.1。
2. 不同geckodriver（Firefox的webdriver程序）版本，支持的Firefox版本也不相同，具体支持哪些版本，在geckodriver的releases页面上有说明。

测试结果如下图所示。没有再弹出认证窗口，访问http://httpbin.org/ip直接回显了HTTP代理的IP：



### Python + Firefox + 插件（closeproxy.xpi）

其中，closeproxy.xpi 文件，需要 Google、Bing 搜下都能搜到下载地址

完整的测试代码如下：
```py
'''
# Python + Selenium + Firefox 设置密码时，需要使用到两个插件：
# 插件1： modify_headers-0.7.1.1-fx.xpi
# 下载地址：https://github.com/mimvp/mimvp-proxy-demo
#
# 方式2： close_proxy_authentication-1.1.xpi
# 下载地址：https://github.com/mimvp/mimvp-proxy-demo
'''
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.proxy import *
from pyvirtualdisplay import Display
from base64 import b64encode
 
 
proxy = {
    "host": "123.57.78.100",
    "port": "12345",
    "user": "username",
    "pass": "password"
}
 
profile = webdriver.FirefoxProfile()
 
# add new header
profile.add_extension("modify_headers-0.7.1.1-fx.xpi")
profile.set_preference("extensions.modify_headers.currentVersion", "0.7.1.1-fx")
profile.set_preference("modifyheaders.config.active", True)
profile.set_preference("modifyheaders.headers.count", 1)
profile.set_preference("modifyheaders.headers.action0", "Add")
profile.set_preference("modifyheaders.headers.name0", "Proxy-Switch-Ip")
profile.set_preference("modifyheaders.headers.value0", "yes")
profile.set_preference("modifyheaders.headers.enabled0", True)
 
# add proxy
profile.set_preference('network.proxy.type', 1)
profile.set_preference('network.proxy.http', proxy['host'])
profile.set_preference('network.proxy.http_port', int(proxy['port']))
profile.set_preference('network.proxy.no_proxies_on', 'localhost, 127.0.0.1')
#profile.set_preference("network.proxy.username", 'aaaaa')
#profile.set_preference("network.proxy.password", 'bbbbb')
 
# Proxy auto login
profile.add_extension('closeproxy.xpi')
credentials = '{user}:{pass}'.format(**proxy)
credentials = b64encode(credentials.encode('ascii')).decode('utf-8')
profile.set_preference('extensions.closeproxyauth.authtoken', credentials)
 
profile.update_preferences()
 
driver = webdriver.Firefox(profile)
driver.get("https://proxy.mimvp.com/ip.php")
print driver.page_source
 
driver.quit()
```

### ref
* [firefox代理认证参考：](https://cloud.tencent.com/info/4ebc3027294687320cd3a096dba6f09e.html)
* [selenium firefox设置代理](https://www.cnblogs.com/lgh344902118/p/6339378.html)
* [小白学爬虫-设置Selenium+Chrome代理](https://cuiqingcai.com/4880.html)
* [Python + Selenium + Firefox 使用代理 auth 的用户名密码授权](https://blog.csdn.net/ithomer/article/details/81051721)
* [Python + Selenium + Firefox 如何使用需要auth的代理](https://segmentfault.com/q/1010000007148702/a-1020000007157385)




## ref
* [selenium设置proxy、headers的方法(phantomjs、Chrome、Firefox)](https://www.jb51.net/article/151676.htm)
* [CSDN博主「周小董」](https://blog.csdn.net/xc_zhou/article/details/80823855)
* []()
* []()
* []()
* []()
