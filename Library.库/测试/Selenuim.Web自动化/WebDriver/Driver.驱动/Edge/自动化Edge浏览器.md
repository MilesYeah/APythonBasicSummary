# 自动化Edge浏览器



自动化基于Chromium内核的 微软最新Edge浏览器，首先需要查看Edge的版本。

点击菜单 帮助和反馈 > 关于Microsoft Edge ，在弹出界面中，查看到版本，比如

版本 79.0.309.71 (官方内部版本) (64 位)
然后 点击这里，打开Edge浏览器驱动下载网页 ，并选择下载对应版本的驱动。

在自动化代码中，指定使用Edge Webdriver类，并且指定 Edge 驱动路径，如下所示
```py
from selenium import webdriver

driver = webdriver.Edge(r'd:\tools\webdrivers\msedgedriver.exe')

driver.get('http://www.51job.com')
```

