# Chrome模拟手机浏览器

在做移动端页面测试时可以利用Chrome mobile emulation 辅助完成页面的适配问题，但是目前手机市场上的型号居多我们也没有办法通过人工的模式一一的去适配，所以这里考虑到通过自动化的模式来模拟，下面介绍两种方式通过selenium调用Chrome mobile emulation来完成自动化测试。



## 通过device name模拟的手机型号

```py
import time
from selenium import webdriver

mobileEmulation = {'deviceName': 'Apple iPhone 4'}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)
driver = webdriver.Chrome(chrome_options=options)
driver.get('http://m.baidu.com')
time.sleep(3)
driver.close()
```

## 设置指定分辨率

```py
import time
from selenium import webdriver

WIDTH = 320  # 宽度
HEIGHT = 640  # 高度
PIXEL_RATIO = 3.0  # 分辨率

mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO}}
options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', mobileEmulation)

driver = webdriver.Chrome(chrome_options=options)
driver.get('http://m.baidu.com')

time.sleep(3)
driver.close()
```


## device list

```py
mobile_emulation = {
            "deviceName": "Apple iPhone 3GS",
            "deviceName": "Apple iPhone 4",
            "deviceName": "Apple iPhone 5",
            "deviceName": "Apple iPhone 6",
            "deviceName": "Apple iPhone 6 Plus",
            "deviceName": "BlackBerry Z10",
            "deviceName": "BlackBerry Z30",
            "deviceName": "Google Nexus 4",
            "deviceName": "Google Nexus 5",
            "deviceName": "Google Nexus S",
            "deviceName": "HTC Evo, Touch HD, Desire HD, Desire",
            "deviceName": "HTC One X, EVO LTE",
            "deviceName": "HTC Sensation, Evo 3D",
            "deviceName": "LG Optimus 2X, Optimus 3D, Optimus Black",
            "deviceName": "LG Optimus G",
            "deviceName": "LG Optimus LTE, Optimus 4X HD" ,
            "deviceName": "LG Optimus One",
            "deviceName": "Motorola Defy, Droid, Droid X, Milestone",
            "deviceName": "Motorola Droid 3, Droid 4, Droid Razr, Atrix 4G, Atrix 2",
            "deviceName": "Motorola Droid Razr HD",
            "deviceName": "Nokia C5, C6, C7, N97, N8, X7",
            "deviceName": "Nokia Lumia 7X0, Lumia 8XX, Lumia 900, N800, N810, N900",
            "deviceName": "Samsung Galaxy Note 3",
            "deviceName": "Samsung Galaxy Note II",
            "deviceName": "Samsung Galaxy Note",
            "deviceName": "Samsung Galaxy S III, Galaxy Nexus",
            "deviceName": "Samsung Galaxy S, S II, W",
            "deviceName": "Samsung Galaxy S4",
            "deviceName": "Sony Xperia S, Ion",
            "deviceName": "Sony Xperia Sola, U",
            "deviceName": "Sony Xperia Z, Z1",
            "deviceName": "Amazon Kindle Fire HDX 7″",
            "deviceName": "Amazon Kindle Fire HDX 8.9″",
            "deviceName": "Amazon Kindle Fire (First Generation)",
            "deviceName": "Apple iPad 1 / 2 / iPad Mini",
            "deviceName": "Apple iPad 3 / 4",
            "deviceName": "BlackBerry PlayBook",
            "deviceName": "Google Nexus 10",
            "deviceName": "Google Nexus 7 2",
            "deviceName": "Google Nexus 7",
            "deviceName": "Motorola Xoom, Xyboard",
            "deviceName": "Samsung Galaxy Tab 7.7, 8.9, 10.1",
            "deviceName": "Samsung Galaxy Tab",
            "deviceName": "Notebook with touch",
            "deviceName": "iPhone 6"
}
```






# ref
* [python selenium Chrome模拟手机浏览器（十七）](https://www.cnblogs.com/mengyu/p/8117881.html)
* [python之selenium设置浏览器为手机模式（开发者模式）](https://blog.csdn.net/qq_42623386/article/details/123391709)
* []()
* []()
* []()
* []()
* []()
* []()
* []()

