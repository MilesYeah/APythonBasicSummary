# Http 代理 phantomjs


## 设置代理
### 方法1：
```py
service_args = [
    '--proxy=%s' % ip_html,  # 代理 IP：prot  （eg：192.168.0.28:808）
    '--proxy-type=http',      # 代理类型：http/https
    '--load-images=no',      # 关闭图片加载（可选）
    '--disk-cache=yes',      # 开启缓存（可选）
    '--ignore-ssl-errors=true'  # 忽略https错误（可选）
]
driver = webdriver.PhantomJS(service_args=service_args)
```



### 方法2：

```py
browser=webdriver.PhantomJS(PATH_PHANTOMJS)

# 利用DesiredCapabilities(代理设置)参数值，重新打开一个sessionId，我看意思就相当于浏览器清空缓存后，加上代理重新访问一次url
proxy=webdriver.Proxy()
proxy.proxy_type=ProxyType.MANUAL
proxy.http_proxy='1.9.171.51:800'

# 将代理设置添加到webdriver.DesiredCapabilities.PHANTOMJS中
proxy.add_to_capabilities(webdriver.DesiredCapabilities.PHANTOMJS)
browser.start_session(webdriver.DesiredCapabilities.PHANTOMJS)
browser.get('http://1212.ip138.com/ic.asp')

print('1: ',browser.session_id)
print('2: ',browser.page_source)
print('3: ',browser.get_cookies())
```



### 还原为系统代理

```py
# 还原为系统代理
proxy=webdriver.Proxy()
proxy.proxy_type=ProxyType.DIRECT
proxy.add_to_capabilities(webdriver.DesiredCapabilities.PHANTOMJS)
browser.start_session(webdriver.DesiredCapabilities.PHANTOMJS)
browser.get('http://1212.ip138.com/ic.asp')
```



## 设置请求头
### 方法2

```py
import random,requests,json
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.proxy import ProxyType


#随机获取一个ip
def proxies():
    r = requests.get("http://120.26.166.214:9840/JProxy/update/proxy/scoreproxy")
    rr = json.loads(r.text)
    hh = rr['ip'] + ":" + "8907"
    print(hh)
    return hh
ips =proxies()


#设置phantomjs请求头和代理方法一：
#-------------------------------------------------------------------------------------
# 设置代理
service_args = [
    '--proxy=%s' % ips,         # 代理 IP：prot  （eg：192.168.0.28:808）
    '--ssl-protocol=any',       # 忽略ssl协议
    '--load - images = no',     # 关闭图片加载（可选）
    '--disk-cache=yes',         # 开启缓存（可选）
    '--ignore-ssl-errors=true'  # 忽略https错误(可选)
]

#设置请求头
user_agent = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) " +
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36"
  )
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = user_agent
driver = webdriver.PhantomJS(executable_path=r"C:\soft\phantomjs-2.1.1-windows\bin\phantomjs.exe",
               desired_capabilities=dcap,service_args=service_args)

driver.get(url='http://www.baidu.com')
page=driver.page_source
print(page)

#设置phantomjs请求头和代理方法二：
#-------------------------------------------------------------------------------------
desired_capabilities = DesiredCapabilities.PHANTOMJS.copy()
# 从USER_AGENTS列表中随机选一个浏览器头，伪装浏览器
desired_capabilities["phantomjs.page.settings.userAgent"] = (random.choice('请求头池'))

# 不载入图片，爬页面速度会快很多
desired_capabilities["phantomjs.page.settings.loadImages"] = False

# 利用DesiredCapabilities(代理设置)参数值，重新打开一个sessionId，我看意思就相当于浏览器清空缓存后，加上代理重新访问一次url
proxy = webdriver.Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = random.choice('ip池')
proxy.add_to_capabilities(desired_capabilities)
phantomjs_driver = r'C:\phantomjs-2.1.1-windows\bin\phantomjs.exe'
# 打开带配置信息的phantomJS浏览器
driver = webdriver.PhantomJS(executable_path=phantomjs_driver,desired_capabilities=desired_capabilities)
driver.start_session(desired_capabilities)


driver.get(url='http://www.baidu.com')
page=driver.page_source
print(page)


# 隐式等待5秒，可以自己调节
driver.implicitly_wait(5)
# 设置10秒页面超时返回，类似于requests.get()的timeout选项，driver.get()没有timeout选项
# 以前遇到过driver.get(url)一直不返回，但也不报错的问题，这时程序会卡住，设置超时选项能解决这个问题。
driver.set_page_load_timeout(20)
# 设置10秒脚本超时时间
driver.set_script_timeout(20)

#翻页命令
driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
```





## ref
* [selenium设置proxy、headers的方法(phantomjs、Chrome、Firefox)](https://www.jb51.net/article/151676.htm)
* [CSDN博主「周小董」](https://blog.csdn.net/xc_zhou/article/details/80823855)
* []()
* []()
* []()
* []()
