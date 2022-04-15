# Http 代理 chrome

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
# !/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver

# 进入浏览器设置
options = webdriver.ChromeOptions()
# 谷歌无头模式
options.add_argument('--headless')
options.add_argument('--disable-gpu')
# options.add_argument('window-size=1200x600')
# 设置中文
options.add_argument('lang=zh_CN.UTF-8')
# 更换头部
options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
# 设置代理
if proxy:
    options.add_argument('proxy-server=' + proxy)
if user_agent:
    options.add_argument('user-agent=' + user_agent)

browser = webdriver.Chrome(chrome_options=options)
url = "https://httpbin.org/get?show_env=1"
browser.get(url)
browser.quit()

```


## selenium设置chrome–cookie

```py
# !/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
browser = webdriver.Chrome()

url = "https://www.baidu.com/"
browser.get(url)
# 通过js新打开一个窗口
newwindow='window.open("https://www.baidu.com");'
# 删除原来的cookie
browser.delete_all_cookies()
# 携带cookie打开
browser.add_cookie({'name':'ABC','value':'DEF'})
# 通过js新打开一个窗口
browser.execute_script(newwindow)
input("查看效果")
browser.quit()
```



## selenium设置chrome-图片不加载

```py
from selenium import webdriver

options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values': {
        'images': 2
    }
}
options.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(chrome_options=options)

# browser = webdriver.Chrome()
url = "http://image.baidu.com/"
browser.get(url)
input("是否有图")
browser.quit()
```



## Chrome设置代理(认证)
默认情况下，Chrome的 `–proxy-server="http://ip:port"` 参数不支持设置用户名和密码认证。这样就使得"Selenium + Chrome Driver"无法使用HTTP Basic Authentication的HTTP代理。

一种变通的方式就是采用IP地址认证，但在国内网络环境下，大多数用户都采用ADSL形式网络接入，IP是变化的，也无法采用IP地址绑定认证。因此迫切需要找到一种让Chrome自动实现HTTP代理用户名密码认证的方案。

Stackoverflow上有人分享了一种利用Chrome插件实现自动代理用户密码认证的方案非常不错，
[详细地址](http://stackoverflow.com/questions/9888323/how-to-override-basic-authentication-in-selenium2-with-java-using-chrome-driver)。

鲲之鹏的技术人员在该思路的基础上用 Python 实现了自动化的Chrome插件创建过程，即根据指定的代理“username:password@ip:port”自动创建一个Chrome代理插件，
然后就可以在"Selenium + Chrome Driver"中通过安装该插件实现代理配置功能，具体代码如下:

```py
# -*- coding:utf-8 -*-
# 测试"Selenium + Chrome"使用带用户名密码认证的代理
import os,re,time,zipfile
from selenium import webdriver


# Chrome代理模板插件(https://github.com/RobinDev/Selenium-Chrome-HTTP-Private-Proxy)目录
CHROME_PROXY_HELPER_DIR = 'chrome-proxy-extensions\Chrome-proxy-helper'
# 存储自定义Chrome代理扩展文件的目录
CUSTOM_CHROME_PROXY_EXTENSIONS_DIR = 'chrome-proxy-extensions'

def get_chrome_proxy_extension(proxy):
    """获取一个Chrome代理扩展,里面配置有指定的代理(带用户名密码认证)
    proxy - 指定的代理,格式: username:password@ip:port
    """
    m = re.compile('([^:]+):([^\@]+)\@([\d\.]+):(\d+)').search(proxy)
    if m:
        # 提取代理的各项参数
        username = m.groups()[0]
        password = m.groups()[1]
        ip = m.groups()[2]
        port = m.groups()[3]
        # print(username,password,ip,port)
        # 创建一个定制Chrome代理扩展(zip文件)
        if not os.path.exists(CUSTOM_CHROME_PROXY_EXTENSIONS_DIR):
            os.mkdir(CUSTOM_CHROME_PROXY_EXTENSIONS_DIR)
        extension_file_path = os.path.join(CUSTOM_CHROME_PROXY_EXTENSIONS_DIR, '{}.zip'.format(proxy.replace(':', '_')))
        if not os.path.exists(extension_file_path):
            # 扩展文件不存在，创建
            zf = zipfile.ZipFile(extension_file_path, mode='w')
            if not os.path.exists(CHROME_PROXY_HELPER_DIR):
                os.mkdir(CHROME_PROXY_HELPER_DIR)
            zf.write(os.path.join(CHROME_PROXY_HELPER_DIR, 'manifest.json'), 'manifest.json')
            # 替换模板中的代理参数
            background_content = open(os.path.join(CHROME_PROXY_HELPER_DIR, 'background.js')).read()
            background_content = background_content.replace('%proxy_host', ip)
            background_content = background_content.replace('%proxy_port', port)
            background_content = background_content.replace('%username', username)
            background_content = background_content.replace('%password', password)
            zf.writestr('background.js', background_content)
            zf.close()
        # print(extension_file_path)
        return extension_file_path
    else:
        raise Exception('Invalid proxy format. Should be username:password@ip:port')


if __name__ == '__main__':
    # 测试
    options = webdriver.ChromeOptions()
    # 添加一个自定义的代理插件（配置特定的代理，含用户名密码认证）
    options.add_extension(get_chrome_proxy_extension(proxy='username:password@ip:port'))
    driver = webdriver.Chrome(chrome_options=options, executable_path='./source/chromedriver_win32_2.35/chromedriver.exe')
    # 访问一个IP回显网站，查看代理配置是否生效了
    driver.get('http://httpbin.org/ip')
    # driver.get('http://ip138.com/')
    # driver.get('http://www.baidu.com/')
    # driver.get('https://www.google.com.hk/search?q=%E6%B8%A4%E6%B5%B7%E9%87%91%E6%8E%A7&safe=strict&tbs=sbd:1&tbm=nws&ei=&start=10&sa=N&biw=&bih=&dpr=1')
    # print(driver.page_source)
    time.sleep(60)
    driver.quit()
```



### 测试结果如下所示：
```json
{
  "origin": "192.168.8.84"
}
```


### 其它
```py
# -*- coding: utf-8 -*-
import time,string,zipfile,os
from selenium import webdriver

def create_proxyauth_extension(proxy_host, proxy_port,proxy_username, proxy_password,
                               scheme='http', plugin_path=None):
    """Proxy Auth Extension
    args:
        proxy_host (str): domain or ip address, ie proxy.domain.com
        proxy_port (int): port
        proxy_username (str): auth username
        proxy_password (str): auth password
    kwargs:
        scheme (str): proxy scheme, default http
        plugin_path (str): absolute path of the extension

    return str -> plugin_path
    """
    if plugin_path is None:
        file='./chrome_proxy_helper'
        if not os.path.exists(file):
            os.mkdir(file)
        plugin_path = file+'/%s_%s@%s_%s.zip'%(proxy_username,proxy_password,proxy_host,proxy_port)

    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Chrome Proxy",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"
        ],
        "background": {
            "scripts": ["background.js"]
        },
        "minimum_chrome_version":"22.0.0"
    }
    """
    background_js = string.Template(
    """
    var config = {
            mode: "fixed_servers",
            rules: {
              singleProxy: {
                scheme: "${scheme}",
                host: "${host}",
                port: parseInt(${port})
              },
              bypassList: ["foobar.com"]
            }
          };

    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

    function callbackFn(details) {
        return {
            authCredentials: {
                username: "${username}",
                password: "${password}"
            }
        };
    }

    chrome.webRequest.onAuthRequired.addListener(
                callbackFn,
                {urls: ["<all_urls>"]},
                ['blocking']
    );
    """
    ).substitute(
        host=proxy_host,
        port=proxy_port,
        username=proxy_username,
        password=proxy_password,
        scheme=scheme,
    )
    with zipfile.ZipFile(plugin_path, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)

    return plugin_path


if __name__=='__main__':
    proxyauth_plugin_path = create_proxyauth_extension(
        proxy_host="139.92.6.230",
        proxy_port=3100,
        proxy_username="",
        proxy_password="",
        scheme='http'
    )
    options = webdriver.ChromeOptions()
    #浏览器最大化
    options.add_argument("--start-maximized")
    #增加扩展
    options.add_extension(proxyauth_plugin_path)
    driver = webdriver.Chrome(chrome_options=options,executable_path='../source/chromedriver_win32_2.40/chromedriver.exe')
    driver.get("http://httpbin.org/ip")
    # driver.get('http://ip138.com/')
    # driver.get('https://www.google.com.hk/search?q=%E6%B8%A4%E6%B5%B7%E9%87%91%E6%8E%A7&safe=strict&tbs=sbd:1&tbm=nws&ei=&start=10&sa=N&biw=&bih=&dpr=1')
    # print(driver.page_source)
    time.sleep(10)
    driver.quit()
```








## ref
* [selenium设置proxy、headers的方法(phantomjs、Chrome、Firefox)](https://www.jb51.net/article/151676.htm)
* [CSDN博主「周小董」](https://blog.csdn.net/xc_zhou/article/details/80823855)
* [插件源代码](https://github.com/RobinDev/Selenium-Chrome-HTTP-Private-Proxy)
* [chrome代理认证参考：](https://www.cnblogs.com/rookies/p/6119786.html)
* [chrome代理认证参考：](https://www.cnblogs.com/roystime/p/6935543.html)
* [参考：](https://www.zhihu.com/question/35547395)
* []()
* []()
* []()
* []()
