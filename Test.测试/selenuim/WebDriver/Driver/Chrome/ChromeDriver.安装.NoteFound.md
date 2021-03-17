

安装chromedriver
 下载
chromedriver的版本一定要与Chrome的版本一致，不然就不起作用。

有两个下载地址：

1、http://chromedriver.storage.googleapis.com/index.html

2、https://npm.taobao.org/mirrors/chromedriver/

当然，你首先需要查看你的Chrome版本，在浏览器中输入chrome://version/,在新的页面中我们得到如下信息。
由此可见，chrome 版本为 `88.0.4324.190`.
```
Google Chrome	88.0.4324.190 (正式版本) （64 位） (cohort: binary_size_exp_1mb )
修订版本	3a97857a62ee2a8b3f6561ccd98b9e0436604cbe-refs/branch-heads/4324_182@{#3}
操作系统	Windows 10 OS Version 1803 (Build 17134.1304)
JavaScript	V8 8.8.278.17
用户代理	Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36
命令行	"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --flag-switches-begin --flag-switches-end --origin-trial-disabled-features=SecurePaymentConfirmation
可执行文件路径	C:\Program Files (x86)\Google\Chrome\Application\chrome.exe
个人资料路径	C:\Users\robert.ye\AppData\Local\Google\Chrome\User Data\Default
其他变体	af81735d-ca7d8d80
84085631-ab02a1cf
90a7075b-12ede6a2
```

如果可以翻墙，我们可以使用网址1直接到google 网站查找driver，使用网址2也可以找到 chrome 驱动，如下表。
我们需要找到与机器上安装的 Chrome 版本一致的驱动，但当前列表中并没有一模一样的，那么我们选择一个版本最接近的驱动 `88.0.4324.96`。
```
Mirror index of http://chromedriver.storage.googleapis.com/
../
2.0/                                              2013-09-25T22:57:39.349Z                          -
2.1/                                              2013-09-25T22:57:49.481Z                          -
2.10/                                             2014-05-01T20:46:22.843Z                          -
2.11/                                             2014-10-08T01:17:17.918Z                          -
2.12/                                             2014-10-27T09:27:24.626Z                          -
2.13/                                             2014-12-10T13:17:59.776Z                          -

...

88.0.4324.27/                                     2020-12-03T18:04:37.346Z                          -
88.0.4324.96/                                     2021-01-20T19:01:11.632Z                          -
89.0.4389.23/                                     2021-01-28T17:30:52.195Z                          -
icons/                                            2013-09-25T17:42:04.972Z                          -
70.0.3538.LATEST_RELEASE                          2018-09-19T22:24:28.963Z                          12(12B)

...

```


进入驱动对应链接，下载当前对应系统版本。
```
Mirror index of http://chromedriver.storage.googleapis.com/88.0.4324.96/
../
chromedriver_linux64.zip                          2021-01-20T19:13:52.149Z                          5685461(5.42MB)
chromedriver_mac64.zip                            2021-01-20T19:13:53.953Z                          8137203(7.76MB)
chromedriver_mac64_m1.zip                         2021-01-20T19:13:55.615Z                          7324938(6.99MB)
chromedriver_win32.zip                            2021-01-20T19:13:57.346Z                          5625092(5.36MB)
notes.txt                                         2021-01-20T19:01:19.121Z                          221(221B)
```


## 配置
解压压缩包，找到chromedriver.exe复制到chrome的安装目录（其实也可以随便放一个文件夹）。复制chromedriver.exe文件的路径并加入到电脑的环境变量中去。具体的：

进入环境变量编辑界面，添加到用户变量即可，双击PATH，将你的文件位置（C:\Program Files (x86)\Google\Chrome\Application\）添加到后面。

完成后在cmd下输入chromedriver验证是否安装成功：

```bat
Microsoft Windows [Version 10.0.17134.1304]
(c) 2018 Microsoft Corporation. All rights reserved.

F:\Mirror\Software\Google\Chrome\chromedriver_win32>chromedriver.exe
Starting ChromeDriver 88.0.4324.96 (68dba2d8a0b149a1d3afac56fa74648032bcf46b-refs/branch-heads/4324@{#1784}) on port 9515
Only local connections are allowed.
Please see https://chromedriver.chromium.org/security-considerations for suggestions on keeping ChromeDriver safe.
ChromeDriver was started successfully.
^C
F:\Mirror\Software\Google\Chrome\chromedriver_win32>
```

##  测试
未配置环境也可以，例如：
```py
from selenium import webdriver
import time

def main():
    chrome_driver = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'  #chromedriver的文件位置
    b = webdriver.Chrome(executable_path = chrome_driver)
    b.get('https://www.baidu.com')
    time.sleep(5)
    b.quit()

if __name__ == '__main__':
    main()
```

已配置环境变量时
```py
from selenium import webdriver
import time

def main():
    b = webdriver.Chrome()
    b.get('https://www.baidu.com')
    time.sleep(5)
    b.quit()

if __name__ == '__main__':
    main()
```
