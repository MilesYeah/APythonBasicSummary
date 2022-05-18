# 自动化Electron程序

Electron程序都是基于基于Chromium技术开发的，所以基本也可以用Chromedriver驱动自动化。

要自动化，首先需要得到内置 Chromium的版本号。

向开发人员查询打开 Dev Tools 窗口的快捷键（通常是ctrl + Shift + I），打开Dev Tools 窗口后， 在 Console tab中输入 如下语句，查看版本
```py
> navigator.appVersion.match(/.*Chrome\/([0-9\.]+)/)[1]
  "79.0.3945.130"
```
然后去 chromedriver下载网址 ，下载对应版本的驱动。

在自动化程序中需要指定打开的可执行程序为Electron程序，而不是 Chrome浏览器。

如下所示
```py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

ops = Options()

# 指定Electron程序路径
ops.binary_location = r"C:\electronAPP.exe"

driver = webdriver.Chrome(r"e:\chromedriver.exe", options = ops)
```



