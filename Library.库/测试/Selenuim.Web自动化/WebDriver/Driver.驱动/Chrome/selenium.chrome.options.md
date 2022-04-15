# Chrome Options

Chrome Options常用的行为一般有以下几种：

1. 禁止图片和视频的加载：提升网页加载速度。
2. 添加代理：用于翻墙访问某些页面，或者应对IP访问频率限制的反爬技术。
3. 使用移动头：访问移动端的站点，一般这种站点的反爬技术比较薄弱。
4. 添加扩展：像正常使用浏览器一样的功能。
5. 设置编码：应对中文站，防止乱码。
6. 阻止JavaScript执行
7. ...

Chrome Options是一个配置chrome启动时属性的类，通过这个参数我们可以为Chrome添加如下参数：
| 参数                    | 描述                       |
| ----------------------- | -------------------------- |
| binary_location         | 设置 chrome 二进制文件位置 |
| add_argument            | 添加启动参数               |
| add_extension           | 添加扩展应用               |
| add_encoded_extension   | 添加扩展应用               |
| add_experimental_option | 添加实验性质的设置参数     |
| debugger_address        | 设置调试器地址             |
|                         |                            |



## 常用 Options 参数
| 描述                                               | 参数                                                                                                                                                                                                      |
| -------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 浏览器不提供可视化页面.                            | `options.add_argument('--headless')`     linux下如果系统不支持可视化不加这条会启动失败                                                                                                                    |
| 浏览器不提供可视化页面.                            | `options.add_argument('headless')`                                                                                                                                                                        |
| 指定用户客户端-模拟手机浏览                        | `options.add_argument('user-agent="MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"')` |
| 禁用图片加载, 提升速度                             | `options.add_argument('blink-settings=imagesEnabled=false')`                                                                                                                                              |
| 隐身模式（无痕模式）                               | `options.add_argument('incognito')`                                                                                                                                                                       |
| 自动打开开发者工具                                 | `options.add_argument("auto-open-devtools-for-tabs")`                                                                                                                                                     |
| 设置窗口尺寸，注意宽高之间使用逗号而不是x          | `options.add_argument('window-size=300,600')`                                                                                                                                                             |
| 设置窗口启动位置（左上角坐标）                     | `options.add_argument('window-position=120,0')`                                                                                                                                                           |
| 禁用gpu渲染, 谷歌文档提到需要加上这个属性来规避bug | `options.add_argument('disable-gpu')`                                                                                                                                                                     |
| 全屏启动                                           | `options.add_argument('start-fullscreen')`                                                                                                                                                                |
| 全屏启动，无地址栏                                 | `options.add_argument('kiosk')`                                                                                                                                                                           |
| 启动时，不激活（前置）窗口                         | `options.add_argument('no-startup-window')`                                                                                                                                                               |
|                                                    |                                                                                                                                                                                                           |
| 禁止策略化                                         | `options.add_argument('--disable-infobars')`                                                                                                                                                              |
| 解决DevToolsActivePort文件不存在的报错             | `options.add_argument('--no-sandbox')`                                                                                                                                                                    |
| 谷歌文档提到需要加上这个属性来规避bug              | `options.add_argument('--disable-gpu')`                                                                                                                                                                   |
| 禁用javascript                                     | `options.add_argument('--disable-javascript')`                                                                                                                                                            |
| 最大化运行（全屏窗口）,不设置，取元素会报错        | `options.add_argument('--start-maximized')`                                                                                                                                                               |
| 禁用浏览器正在被自动化程序控制的提示               | `options.add_argument('--disable-infobars')`                                                                                                                                                              |
| 隐藏滚动条, 应对一些特殊页面                       | `options.add_argument('--hide-scrollbars')`                                                                                                                                                               |
| 不加载图片, 提升速度                               | `options.add_argument('blink-settings=imagesEnabled=false')`                                                                                                                                              |
| 手动指定使用的浏览器位置                           | `options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"`                                                                                                                |
|                                                    |                                                                                                                                                                                                           |
|                                                    |                                                                                                                                                                                                           |



## 手机模式
我们可以通过 desired_capabilities 参数，指定以手机模式打开chrome浏览器

参考代码，如下
```py
from selenium import webdriver

mobile_emulation = {"deviceName": "Nexus 5"}

chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

driver = webdriver.Chrome(desired_capabilities=chrome_options.to_capabilities())

driver.get('http://www.baidu.com')

input("Press anykey to continue...")
driver.quit()

```





## 针对编码格式的操作
```py
# 设置默认编码为 utf-8
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('lang=zh_CN.UTF-8')
driver = webdriver.Chrome(chrome_options = options)
```



## 针对UA请求头的操作

```py
# 设置请求头为huaweiMeta10 Pro
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('User-Agent=Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36')
options.add_argument('--headless')  # 浏览器不提供可视化页面
driver = webdriver.Chrome(chrome_options = options)
```

http://www.fynas.com/ua



## 针对禁止加载图片的操作

```py
# 设置浏览器禁止加载图片
from selenium import webdriver
options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options = options)
```



## 针对IP代理的操作

特别需要注意，在选择代理时，尽量选择静态IP，才能提升爬取的稳定性。如果使用动态匿名IP，每个IP的存活时间是很短的。

```py
# 设置无账号密码的代理
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--proxy-server=http://ip:port')  
driver = webdriver.Chrome(chrome_options=chromeOptions)
```

```py
# 设置有账号密码的代理
proxyauth_plugin_path = create_proxyauth_extension(
            proxy_host='host',
            proxy_port='port',
            proxy_username="username",
            proxy_password="password"
        )
options.add_extension(proxyauth_plugin_path)
```

查看IP地址的链接：http://httpbin.org/ip



## 针对添加插件的操作

```py
# 添加xpath helper应用

from selenium import webdriver
chrome_options = webdriver.ChromeOptions()

# 设置好应用扩展
extension_path = 'your file_path'
chrome_options.add_extension(extension_path)
```



## 针对登录时关闭弹出的密码保存提示框

```py
from selenium import webdriver 
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions() 
prefs = {} 
# 设置这两个参数就可以避免密码提示框的弹出
prefs['credentials_enable_service'] = False 
prefs['profile.password_manager_enabled'] = False 
options.add_experimental_option('prefs', prefs) 
browser = webdriver.Chrome(chrome_options=options) 
browser.get('https://www.baidu.com/')
browser.quit()
```

 
## Chrome 使用 options 配置最大化打开

通过设置 chrome_options 参数达到默认最大化的效果，示例代码：
```py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('start-maximized')
driver=webdriver.Chrome(chrome_options=chrome_options)
```

或者：
```py
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
driver=webdriver.Chrome(chrome_options=options)
```








## Ref
* [List of Chromium Command Line Switches](https://peter.sh/experiments/chromium-command-line-switches/)
* [python+selenium+Chrome options参数](https://www.cnblogs.com/yangjintao/p/10599868.html)
* [RPA手把手——selenium 使 Chrome 默认最大化打开](https://blog.csdn.net/weixin_44447687/article/details/100889222)
* []()
* []()
