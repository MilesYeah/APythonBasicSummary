# 远程WebDriver客户端

要运行远程WebDriver客户端, 我们首先需要连接到RemoteWebDriver. 为此, 我们将URL指向运行测试的服务器的地址. 为了自定义我们的配置, 我们设置了既定的功能. 下面是一个实例化样例, 其指向我们的远程Web服务器 www.example.com 的远程WebDriver对象, 并在Firefox上运行测试.

```py
from selenium import webdriver

firefox_options = webdriver.FirefoxOptions()
driver = webdriver.Remote(
    command_executor='http://www.example.com',
    options=firefox_options
)
driver.get("http://www.google.com")
driver.quit() 
```
  
为了进一步自定义测试配置, 我们可以添加其他既定的功能.

## 浏览器选项
例如, 假设您想使用Chrome版本67 在Windows XP上运行Chrome:

```py
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.set_capability("browserVersion", "67")
chrome_options.set_capability("platformName", "Windows XP")
driver = webdriver.Remote(
    command_executor='http://www.example.com',
    options=chrome_options
)
driver.get("http://www.google.com")
driver.quit()  
```
  
## 本地文件检测器
本地文件检测器允许将文件从客户端计算机传输到远程服务器. 例如, 如果测试需要将文件上传到Web应用程序, 则远程WebDriver可以在运行时 将文件从本地计算机自动传输到远程Web服务器. 这允许从运行测试的远程计算机上载文件. 默认情况下未启用它, 可以通过以下方式启用:

```py
from selenium.webdriver.remote.file_detector import LocalFileDetector

driver.file_detector = LocalFileDetector()
```
  
定义上述代码后, 您可以通过以下方式在测试中上传文件:

```py
driver.get("http://sso.dev.saucelabs.com/test/guinea-file-upload")

driver.find_element(By.ID, "myfile").send_keys("/Users/sso/the/local/path/to/darkbulb.jpg")
```



